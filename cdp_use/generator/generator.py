#!/usr/bin/env python3
"""
Main CDP generator script.

Generates Python type-safe bindings for Chrome DevTools Protocol.
"""

import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

from .command_generator import CommandGenerator
from .event_generator import EventGenerator
from .library_generator import LibraryGenerator
from .registration_generator import RegistrationGenerator
from .registration_library_generator import RegistrationLibraryGenerator
from .registry_generator import RegistryGenerator
from .type_generator import TypeGenerator


class CDPGenerator:
    def __init__(self, output_dir: str = "cdp_use/cdp"):
        self.output_dir = Path(output_dir)
        self.type_generator = TypeGenerator()
        self.command_generator = CommandGenerator()
        self.event_generator = EventGenerator()
        self.library_generator = LibraryGenerator()
        self.registration_generator = RegistrationGenerator()
        self.registration_library_generator = RegistrationLibraryGenerator()
        self.registry_generator = RegistryGenerator()

    def get_auto_generated_header(self) -> str:
        """Get the standard auto-generated file header."""
        return """# This file is auto-generated by the CDP protocol generator.
# Do not edit this file manually as your changes will be overwritten.
# Generated from Chrome DevTools Protocol specifications.

"""

    def load_protocols(
        self, protocol_files: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Load and merge multiple protocol JSON files."""
        if protocol_files is None:
            import sys

            if len(sys.argv) < 2:
                raise ValueError("Please provide at least one protocol JSON file path")
            protocol_files = sys.argv[1:]
        merged_protocol = {"version": {"major": "1", "minor": "0"}, "domains": []}
        seen_domains = set()

        for file_path in protocol_files:
            print(f"Loading protocol file: {file_path}")
            with open(file_path, "r") as f:
                protocol = json.load(f)

            for domain in protocol.get("domains", []):
                domain_name = domain["domain"]
                if domain_name not in seen_domains:
                    merged_protocol["domains"].append(domain)
                    seen_domains.add(domain_name)

        print(
            f"Merged {len(merged_protocol['domains'])} domains from {len(protocol_files)} files"
        )
        return merged_protocol

    def clean_output_dir(self) -> None:
        """Clean the output directory."""
        if self.output_dir.exists():
            import shutil

            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)

    def format_directory(self) -> None:
        """Format the generated code using ruff."""
        try:
            result = subprocess.run(
                ["ruff", "check", "--fix", "--unsafe-fixes", str(self.output_dir)],
                capture_output=True,
                text=True,
                timeout=60,
            )
            if result.returncode != 0:
                print(
                    f"Ruff formatting warnings/errors:\n{result.stdout}\n{result.stderr}"
                )
            else:
                print("Code formatting completed successfully.")
        except subprocess.TimeoutExpired:
            print("Ruff formatting timed out after 60 seconds.")
        except FileNotFoundError:
            print("Ruff not found. Install with: pip install ruff")
        except Exception as e:
            print(f"Error running ruff: {e}")

    def generate_all(self, protocol_files: Optional[List[str]] = None) -> None:
        """Generate all types, commands, events, and protocol classes."""
        protocol = self.load_protocols(protocol_files)
        domains = protocol.get("domains", [])

        print(f"Generating CDP types for {len(domains)} domains...")

        # Clean output directory
        self.clean_output_dir()

        # Generate for each domain
        for domain in domains:
            self.generate_domain(domain)

        # Generate domain library files
        for domain in domains:
            self.generate_domain_library_file(domain)

        # Generate domain registration files
        for domain in domains:
            self.generate_domain_registration_file(domain)

        # Generate main library file
        self.generate_main_library_file(domains)

        # Generate central event registry
        self.generate_event_registry(domains)

        # Generate main registration library
        self.generate_main_registration_library(domains)

        # Generate main __init__.py
        self.generate_main_init(domains)

        print("Generation complete!")

        # Format generated code
        print("Formatting generated code...")
        self.format_directory()

    def generate_domain(self, domain: Dict[str, Any]) -> None:
        """Generate types, commands, and events for a single domain."""
        domain_name = domain["domain"]
        print(f"  Generating {domain_name}...")

        # Create domain directory
        domain_dir = self.output_dir / domain_name.lower()
        domain_dir.mkdir(exist_ok=True)

        # Generate types
        types_content = self.type_generator.generate_types(domain)
        self.write_file(domain_dir / "types.py", types_content)

        # Generate commands
        commands_content = self.command_generator.generate_commands(domain)
        self.write_file(domain_dir / "commands.py", commands_content)

        # Generate events
        events_content = self.event_generator.generate_events(domain)
        self.write_file(domain_dir / "events.py", events_content)

        # Generate domain __init__.py
        init_content = self.generate_domain_init(domain)
        self.write_file(domain_dir / "__init__.py", init_content)

    def generate_domain_library_file(self, domain: Dict[str, Any]) -> None:
        """Generate a domain-specific library file."""
        domain_name = domain["domain"].lower()
        domain_dir = self.output_dir / domain_name
        content = self.library_generator.generate_domain_library(domain)
        self.write_file(domain_dir / "library.py", content)

    def generate_domain_registration_file(self, domain: Dict[str, Any]) -> None:
        """Generate a domain-specific registration file."""
        domain_name = domain["domain"].lower()
        domain_dir = self.output_dir / domain_name
        content = self.registration_generator.generate_registration(domain)
        self.write_file(domain_dir / "registration.py", content)

    def generate_main_library_file(self, domains: List[Dict[str, Any]]) -> None:
        """Generate the main library file."""
        content = self.library_generator.generate_main_library(domains)
        self.write_file(self.output_dir / "library.py", content)

    def generate_event_registry(self, domains: List[Dict[str, Any]]) -> None:
        """Generate the central event registry file."""
        content = self.registry_generator.generate_registry(domains)
        self.write_file(self.output_dir / "registry.py", content)

    def generate_main_registration_library(self, domains: List[Dict[str, Any]]) -> None:
        """Generate the main registration library file."""
        content = self.registration_library_generator.generate_main_registration_library(domains)
        self.write_file(self.output_dir / "registration_library.py", content)

    def generate_domain_init(self, domain: Dict[str, Any]) -> str:
        """Generate __init__.py for a domain."""
        domain_name = domain["domain"]

        # Start with auto-generated header
        content = self.get_auto_generated_header()
        content += f'"""CDP {domain_name} Domain"""\n\n'
        content += "from .types import *\n"
        content += "from .commands import *\n"
        content += "from .events import *\n"

        return content

    def generate_main_init(self, domains: List[Dict[str, Any]]) -> None:
        """Generate main __init__.py file."""
        # Start with auto-generated header
        content = self.get_auto_generated_header()
        content += '"""CDP Type-Safe Client"""\n\n'

        # Import all domains
        for domain in domains:
            domain_name = domain["domain"].lower()
            content += f"from . import {domain_name}\n"

        content += "\nfrom .library import CDPLibrary\n"
        content += "from .registry import EventRegistry\n"
        content += "from .registration_library import CDPRegistrationLibrary\n"

        # List all domains for easy access
        content += "\n__all__ = [\n"
        for domain in domains:
            domain_name = domain["domain"].lower()
            content += f'    "{domain_name}",\n'
        content += '    "CDPLibrary",\n'
        content += '    "EventRegistry",\n'
        content += '    "CDPRegistrationLibrary",\n'
        content += "]\n"

        self.write_file(self.output_dir / "__init__.py", content)

    def write_file(self, path: Path, content: str) -> None:
        """Write content to a file."""
        with open(path, "w") as f:
            f.write(content)


def main():
    generator = CDPGenerator()
    generator.generate_all()


if __name__ == "__main__":
    main()
