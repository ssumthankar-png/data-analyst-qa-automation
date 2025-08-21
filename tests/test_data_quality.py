def test_revenue_calculation():
    revenue = 5000
    cost = 2000
    expected_profit = 3000
    calculated_profit = revenue - cost
    assert calculated_profit == expected_profit, f"Profit mismatch: {calculated_profit} ≠ {expected_profit}"

def test_no_null_emails():
    emails = ["user1@company.com", "user2@gmail.com", None, "user3@yahoo.com"]
    null_emails = [email for email in emails if email is None]
    assert len(null_emails) == 0, f"NULL emails found: {null_emails}"

def test_category_mapping():
    raw_category = "Electronics"
    mapping = {"Electronics": "Tech", "Clothing": "Fashion"}
    assert mapping[raw_category] == "Tech", f"Category '{raw_category}' not mapped correctly"
