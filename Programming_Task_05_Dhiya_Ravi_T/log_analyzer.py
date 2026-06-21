def main():
    login_attempts = ["Success", "Failed", "Failed", "Success", "Failed", "Success"]

    print("=== Cyber Security Log Analyzer ===")
    print("Login Attempts:", login_attempts)

    total_attempts = len(login_attempts)
    successful_logins = login_attempts.count("Success")
    failed_logins = login_attempts.count("Failed")

    print("\n--- Results ---")
    print(f"Total Login Attempts: {total_attempts}")
    print(f"Successful Logins: {successful_logins}")
    print(f"Failed Logins: {failed_logins}")

    print("\n--- Why Monitoring Failed Logins Matters ---")
    print(
        "Repeated failed login attempts can indicate a brute-force attack,\n"
        "where an attacker tries multiple password combinations to gain\n"
        "unauthorized access. Monitoring failed logins helps security teams\n"
        "detect suspicious activity early, identify compromised accounts,\n"
        "and trigger alerts or account lockouts before real damage occurs."
    )


if __name__ == "__main__":
    main()