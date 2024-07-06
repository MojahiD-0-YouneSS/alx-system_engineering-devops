
# Postmortem: The Great Sandbox Debacle of 2024

## Issue Summary
**Duration:** The outage lasted for approximately 3 hours, from 09:00 AM to 12:00 PM UTC on July 1, 2024.

**Impact:** Users were unable to upload media files to the YNS Task Management System. Approximately 70% of users attempting to add notes with media attachments experienced failure. Text-only notes were unaffected.

**Root Cause:** The root cause was a misconfigured file path, which directed media files to be saved outside the main application directory instead of within it.

---

## Timeline

- **09:00 AM UTC:** ☕ **Issue detected:** User complaints start rolling in, error logs explode.
- **09:10 AM UTC:** 🔍 **Investigation begins:** Engineers suspect a file permission issue.
- **09:30 AM UTC:** 🤔 **Misleading paths:** Several rabbit holes involving file permissions are explored.
- **10:00 AM UTC:** 🐰 **More rabbit holes:** Incorrect assumptions about server configurations.
- **10:30 AM UTC:** 🚨 **Escalation:** Backend team steps in, bringing the cavalry.
- **11:00 AM UTC:** 💡 **Eureka moment:** Incorrect file path identified as the culprit.
- **11:30 AM UTC:** 🔧 **Fix applied:** File path corrected, code deployed.
- **12:00 PM UTC:** 🎉 **Resolution confirmed:** System back to normal, users can upload media files again.

---

## Root Cause and Resolution

**Detailed Cause:** The root cause of the issue was a simple but devastating misconfiguration in the `add_note` function within the `app.py` file. The path for saving uploaded media files was directed to a location outside the main application directory. This misconfiguration caused the system to fail in creating and storing files.

**Detailed Fix:** The fix involved correctly setting the `upload_folder` variable to a subdirectory within the main application directory using the following code:

**python snippet**
    upload_folder = os.path.join(os.path.dirname(__file__), 'uploads' # this should be this 'static/uploads ' )
    if not os.path.exists(upload_folder):
       os.makedirs(upload_folder)

## Corrective and Preventative Measures

**Improvements/Fixes**:

Code Review: Implement regular code reviews to catch path misconfigurations early.
Automated Testing: Add automated tests to verify file upload functionality.
Enhanced Monitoring: Improve monitoring to detect file upload errors promptly.

**TODO List:**

Patch app.py: Correct the file path for media uploads.
Automated Tests: Implement tests to ensure media files upload correctly.
Monitoring: Add tracking for file upload success and failure rates.
Code Review: Conduct a review to ensure similar issues are not present elsewhere.
Documentation Update: Highlight the importance of correct file path configurations.

## Adding Some Fun (with a Pretty Diagram)

To make this postmortem a bit more engaging, here’s a simple and fun diagram to visualize the issue and resolution process.

       Issue Detected                  Investigation
          ⬇️                                ⬇️
       User Complaints            Misleading Paths Explored
          ⬇️                                ⬇️
       Escalation           🐰 Rabbit Holes of File Permissions
          ⬇️                                ⬇️
       Eureka Moment                Incorrect File Path Found
          ⬇️                                ⬇️
       Fix Applied                File Path Corrected
          ⬇️                                ⬇️
       Resolution Confirmed           System Back to Normal

## Conclusion

i conclude In the face of adversity, we learned the importance of thorough investigation and the value of simple fixes. By implementing these corrective and preventative measures, we aim to safeguard against similar issues in the future and ensure a more robust and user-friendly YNS Task Management System. And remember, a little humor and a pretty diagram can go a long way in making even the driest technical reports more palatable!
