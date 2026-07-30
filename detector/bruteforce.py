def detect_bruteforce(parsed_logs):

    failed_login_count = {}

    for log in parsed_logs:

        if log["event"] == "LOGIN_FAILED":

            ip = log["ip"]

            if ip not in failed_login_count:
                failed_login_count[ip] = 0

            failed_login_count[ip] += 1

    return failed_login_count