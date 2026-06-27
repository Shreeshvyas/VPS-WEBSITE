import subprocess
import sys
import time

def main():
    print("Starting automated bubblewrap init...")
    cmd = ["cmd.exe", "/c", "bubblewrap init --manifest=http://127.0.0.1:8000/manifest.json"]
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    buffer = ""
    # Map prompt keywords to our responses
    # We will send specific inputs for critical prompts, and empty line (newline) for defaults
    prompts = [
        ("Domain:", "portal.vyaspublicschool.in\n"),
        ("URL path:", "\n"),
        ("Application name:", "Vyas Public School\n"),
        ("Short name:", "VPHS Portal\n"),
        ("Package ID:", "in.vyaspublicschool.portal\n"),
        ("Version name:", "\n"),
        ("Version code:", "\n"),
        ("Display:", "\n"),
        ("Orientation:", "\n"),
        ("Theme color:", "\n"),
        ("Navigation color:", "\n"),
        ("Navigation color dark:", "\n"),
        ("Background color:", "\n"),
        ("Splash screen fade out duration:", "\n"),
        ("Enable Notifications:", "\n"),
        ("Include location delegation:", "\n"),
        ("Play Billing:", "\n"),
        ("Request geolocation permission:", "\n"),
        ("Signing Key Path:", "\n"),
        ("Key store password:", "vyas123456\n"),
        ("Key password:", "\n"),
        ("First and last name:", "Sanjay Vyas\n"),
        ("organizational unit:", "IT\n"),
        ("organization:", "Vyas Public School\n"),
        ("City or Locality:", "Bhikangaon\n"),
        ("State or Province:", "MP\n"),
        ("two-letter country code:", "IN\n"),
    ]

    # Keep track of which prompts we have responded to
    responded = set()

    # Read output character by character to handle interactive prompts cleanly
    while True:
        char = proc.stdout.read(1)
        if not char:
            break
        sys.stdout.write(char)
        sys.stdout.flush()
        buffer += char

        # Check if any prompt matches
        for p_text, response in prompts:
            if p_text in buffer and p_text not in responded:
                print(f"\n[Auto-Responder] Matched prompt '{p_text}', sending: {repr(response)}")
                proc.stdin.write(response)
                proc.stdin.flush()
                responded.add(p_text)
                buffer = "" # Clear buffer after response
                break

    proc.wait()
    print(f"\nBubblewrap init finished with exit code: {proc.returncode}")

if __name__ == "__main__":
    main()
