import subprocess
import os
import shutil

# ANSI color codes
RED = '\033[91m'
RESET = '\033[0m'

# ASCII art
print(RED)
print("""
                 __     _ ____                         
   ____  __  _______/ /__  (_) __/_  __________  ___  _____
  / __ \/ / / / ___/ / _ \/ / /_/ / / /_  /_  / / _ \/ ___/
 / / / / /_/ / /__/ /  __/ / __/ /_/ / / /_/ /_/  __/ /    
/_/ /_/\__,_/\___/_/\___/_/_/  \__,_/ /___/___/\___/_/   v1.0.2

                           Made by Satya Prakash (0xKayala)
""")
print(RESET)

def display_help():
    print("NucleiFuzzer is a Powerful Automation tool for detecting XSS, SQLi, SSRF, Open-Redirect, etc. vulnerabilities in Web Applications")
    print("\nUsage: python nuclei_fuzzer.py [options]")
    print("\nOptions:")
    print("  -h, --help              Display help information")
    print("  -d, --domain <domain>   Single domain to scan for vulnerabilities")
    print("  -f, --file <filename>   File containing multiple domains/URLs to scan")

def run_paramspider(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    shutil.copy(input_file, os.path.join(output_dir, os.path.basename(input_file)))
    subprocess.run(["python3", "/path/to/ParamSpider/paramspider.py", "-l", "high", "-o", output_dir, "-d", output_dir])

def run_nuclei(input_dir, output_file):
    subprocess.run(["nuclei", "-l", input_dir, "-o", output_file, "-t", "/path/to/fuzzing-templates", "-c", "50"])

def main():
    import argparse
    parser = argparse.ArgumentParser(description="NucleiFuzzer")
    parser.add_argument("-d", "--domain", help="Single domain to scan for vulnerabilities")
    parser.add_argument("-f", "--file", help="File containing multiple domains/URLs to scan")
    args = parser.parse_args()

    if not args.domain and not args.file:
        display_help()
        return

    output_dir = "output"
    output_file = "output/allurls.txt"
    if args.domain:
        run_paramspider(args.domain, output_dir)
        run_nuclei(output_dir, output_file)
    elif args.file:
        with open(args.file, 'r') as file:
            for line in file:
                run_paramspider(line.strip(), output_dir)
        run_nuclei(output_dir, output_file)

    if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
        print("No URLs Found. Exiting...")
        return

    print("Scan is completed - Happy Fuzzing")

if __name__ == "__main__":
    main()
