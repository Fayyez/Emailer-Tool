from emailer import isvalidemail

if __name__ == "__main__":
    raws = [""]
    target = "../receipient_list.txt"
    with open(target, "a") as recipient_file:
        for raw in raws:
            with open(raw, "r", encoding="utf-8", errors="ignore") as raw_file:
                # read entire file
                content = raw_file.read()
                print(content[1:50])
                content = content.split()
                for entry in content:
                    if isinstance(entry, str) and isvalidemail(entry):
                        entry = entry.strip()
                        recipient_file.write(entry + "\n")