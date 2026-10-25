# Test Plan for Portfolio Website Automation

**Target URL:** https://keza250.github.io/kezamillajoie.github.com/
**Module:** Development Operations (ITLDO801) - Assignment 3
**Author:** Keza Millajoie Appoline

## Test Cases Overview

| Test ID | What is Tested | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC-01** | Portfolio Home Page Load | 1. Navigate to portfolio URL.<br>2. Wait for page DOM to load.<br>3. Verify the window title. | Page loads successfully and browser title contains expected text. |
| **TC-02** | About Me Navigation Link | 1. Locate "About Me" link in navigation.<br>2. Click link.<br>3. Verify target section visibility. | Page scrolls/navigates to `#about` section; `#about` element becomes visible in viewport. |
| **TC-03** | Services Navigation Link | 1. Locate "Services Offered" link in navigation.<br>2. Click link.<br>3. Verify target section visibility. | Page scrolls/navigates to `#services` section; `#services` element becomes visible in viewport. |
| **TC-04** | Projects & Achievements Link | 1. Locate "Projects" link in navigation.<br>2. Click link.<br>3. Verify target section visibility. | Page scrolls/navigates to `#projects` section; `#projects` element becomes visible in viewport. |
| **TC-05** | External / GitHub Profile Link | 1. Locate the external repository/GitHub link.<br>2. Click the link.<br>3. Verify target URL. | Browser navigates to or opens the correct external URL (e.g., GitHub profile/repo). |
| **TC-06** | *[Negative Test]* Non-Existent Section | 1. Attempt to locate element with ID `#nonexistent-section`.<br>2. Wait up to 5 seconds. | Locator fails to find element; `NoSuchElementException` or `TimeoutException` is raised and caught cleanly. |
