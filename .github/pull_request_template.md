## Description
Briefly describe the purpose of your pull request by providing a summary of the changes you made.

## TestRail/JIRA Links
**JIRA Ticket:** [AUTO-123](https://yourcompany.atlassian.net/browse/AUTO-123)
**TestRail Test Case(s):** 
- [TC001: Login Functionality](https://yourcompany.testrail.io/index.php?/cases/view/001)
- [TC002: User Registration](https://yourcompany.testrail.io/index.php?/cases/view/002)

## SStack_B1 Framework Information
**Repository:** https://github.com/HarshaKB-TY/SStack_B1.git
**Framework Version:** [Check latest commit]
**Modified Areas:** [List specific framework areas touched]

## Automation Results Link
**Test Execution Report:** [Provide direct link to test execution results - not Jenkins build link]
**Local Test Results:**

pytest tests/your_test.py -v --html=reports/local_results.html
Total Tests: X | Passed: X | Failed: X | Duration: X minutes

**Cross-Browser Results:**
- Chrome: ✅ Pass (X/X tests)
- Firefox: ✅ Pass (X/X tests)  
- Edge: ✅ Pass (X/X tests)

## Changes Made
- [ ] New test cases added
- [ ] Page objects updated/created
- [ ] Bug fixes implemented
- [ ] Framework enhancements
- [ ] Test data updated
- [ ] Documentation updated
- [ ] Configuration changes

## [Self Review Checklist - SStack_B1 Python Framework](https://github.com/HarshaKB-TY/SStack_B1/wiki/Self-Review-Guidelines)
<details>
<summary>Self-review checklist (Click to expand)</summary>

### Test Design & Data Management
- [ ] I have used separate test users/accounts for each test case
- [ ] I have stored URLs in configuration files (config.py/config.json) instead of hardcoding
- [ ] I have passed data as variables from test cases (using TestData class or external files)
- [ ] I have used external test data files (Excel/JSON/CSV) for test data not in configuration
- [ ] I have used descriptive variable names, avoiding abbreviations
- [ ] I have used `PascalCase` for class names and `snake_case` for functions and variables

### Code Quality & Standards
- [ ] I have ensured that unnecessary changes are not shown in code
- [ ] I have avoided committing unused or commented code
- [ ] I have removed any debugging code (print statements, time.sleep, breakpoints)
- [ ] I have checked for typos in code and comments
- [ ] I have named functions based on their actions (e.g., `click_login_button()`)
- [ ] I have merged functions with similar actions by parameterizing them
- [ ] I have added proper docstrings for new methods and classes

### Locator Strategy & Framework Integration
- [ ] I have preferred CSS selectors & element IDs/Names instead of XPath
- [ ] I have used data-testid attributes where available
- [ ] I have avoided creating unnecessary variables and passed values directly if possible
- [ ] I have used SStack_B1 framework functions instead of direct Selenium calls
- [ ] I have used explicit waits (WebDriverWait) instead of time.sleep() or implicit waits
- [ ] I have used framework utility functions for common operations

### Page Object Model & Navigation
- [ ] I have followed Page Object Model pattern consistently
- [ ] Every page interaction method returns the appropriate next page object (where applicable)
- [ ] I have only created utility functions if they interact with 2 or more page objects
- [ ] I have stored locators as class constants in page object classes
- [ ] I have implemented proper page object initialization and validation

### Assertions & Validations
- [ ] I have used descriptive assert statements with clear error messages
- [ ] I have used element text assertions to verify messages rather than just element presence
- [ ] I have validated page navigation and state changes appropriately
- [ ] I have used appropriate assertion methods (assert, assertEqual, assertTrue, etc.)
- [ ] I have verified both positive and negative test scenarios

### Logging & Reporting Integration
- [ ] I have used proper logging with appropriate log levels (Logger.info, Logger.debug, Logger.error)
- [ ] I have used plain English comments to explain test case flow and verifications
- [ ] I have added step-by-step logging for test execution tracking
- [ ] I have integrated with Allure reporting (if using @allure decorators)
- [ ] I have added screenshot capture for test failures

### Test Independence & Reliability
- [ ] My tests can run independently without depending on other tests
- [ ] I have implemented proper test setup and teardown
- [ ] I have used appropriate test fixtures and configurations
- [ ] I have handled potential race conditions and timing issues
- [ ] I have made tests deterministic and repeatable

### Environment & Configuration
- [ ] I have used environment-specific configurations appropriately
- [ ] I have avoided hardcoding environment-specific values
- [ ] I have used virtual environment and proper dependency management
- [ ] I have verified tests work across different environments (dev/staging)
- [ ] I have documented any new configuration requirements

### Documentation & Maintenance
- [ ] I have updated README.md if framework changes were made
- [ ] I have documented any new dependencies or setup requirements
- [ ] I have added comments for complex business logic
- [ ] I have updated test case documentation in TestRail/JIRA
- [ ] I have included migration notes for any breaking changes

</details>

## Test Execution Summary
**Total Tests:** [Number of tests]
**Execution Time:** [Time taken]
**Environment:** [dev/staging/production]
**Browser Coverage:** [Chrome/Firefox/Edge/Safari]
**Python Version:** [3.8+]
**Virtual Environment:** [Activated and dependencies installed]

## Manual Testing Checklist (if applicable)
- [ ] Tested core functionality manually before automation
- [ ] Verified UI elements and user flows
- [ ] Confirmed test data and user accounts work
- [ ] Validated across different browsers manually

## Performance Considerations
- [ ] Tests execute within reasonable time limits (< 5 minutes per test)
- [ ] No unnecessary waits or delays added
- [ ] Efficient locator strategies used
- [ ] Memory usage optimized for long test runs

## Security & Privacy
- [ ] No sensitive data (passwords, tokens, PII) hardcoded
- [ ] Test data follows data privacy regulations
- [ ] Secure handling of test credentials and API keys
- [ ] No production data used in testing

## Breaking Changes
- [ ] No breaking changes introduced
- [ ] If breaking changes exist, migration guide provided
- [ ] Backward compatibility maintained where possible
- [ ] Team notified of any framework changes

## Screenshots/Videos
[Attach screenshots of test execution, new UI elements being tested, or framework enhancements]

## Additional Notes
Add any additional notes, known issues, future improvements planned, or special setup requirements.

## Reviewer Notes
**Areas needing special attention:**
- [Highlight specific areas for reviewers to focus on]
- [Any architectural decisions made]
- [Performance considerations or concerns]
- [Complex logic that needs validation]

## Definition of Done
- [ ] All acceptance criteria met
- [ ] Code reviewed and approved by 2 team members (1 Admin + 1 peer)
- [ ] Tests pass locally and in CI/CD (when available)
- [ ] Documentation updated appropriately
- [ ] No merge conflicts with main branch
- [ ] Ready for production deployment