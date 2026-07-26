def parse_logs(filepath):

    parsed_logs = []

    with open(filepath, "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            parts = line.split()

            timestamp = parts[0] + " " + parts[1]
            level = parts[2]
            event = parts[3]
            user = parts[4].split("=")[1]

            ip = "N/A"

            if len(parts) > 5 and parts[5].startswith("IP="):
                ip = parts[5].split("=")[1]

            parsed_logs.append({
                "timestamp": timestamp,
                "level": level,
                "event": event,
                "user": user,
                "ip": ip
            })

    return parsed_logs