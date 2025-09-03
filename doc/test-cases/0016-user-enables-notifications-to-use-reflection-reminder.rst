=====================================================
User enables notifications to use reflection reminder
=====================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0016
      - 
        * https://github.com/colinfwren/garner/issues/8

====
Setup
====

- There's an existing question in the system
- There's an existing reflection reminder setup

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - 
        * Fresh App Install where no notification permissions have been granted
        * Add a Question to the Question List to be able to use Reflection Reminders
      - 
      - The Reflection Reminder button should say "Enable Notifications"
    * - Press "Enable Notifications" button
      - 
      - A Notification permissions alert is shown
    * - Press "Allow notifications" in the alert
      - 
      - 
        * The app is now allowed to trigger local notifications
        * The Reflection Reminder button now says "Add Reflection Reminder"
    * - Set Daily Reflection Reminder schedule to trigger 2 minutes into the future
      - 
      - 
        * The Reflection Reminder text shows the schedule as daily and set to trigger at the time set
        * The Reflection Reminder button says "Update Reminder"
    * - Close app
      - 
      - The is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - At the time set a local notification is triggered that say it's time for the user to reflect on their day
    * - Dismiss the Notification
      - 
      - The Notification Center has no notifications from Garner in it
    * - 
        * Open the Garner app settings
        * Turn off notifications for the app
      - 
      - The app is no longer permitted to send notifications
    * - Open Garner
      - 
      - 
        * There should be an un-actioned Reflection Reminder prompt in the Reflection List
        * The Reflection Reminder text should say the schedule for the reminder set
        * The Reflection Reminder text should say the reminders are paused due to permission not being granted
        * The Reflection Reminder button should say "Enable notifications in Settings"
    * - Press the "Enable notifications in settings" button
      - 
      - The user is navigated to the Garner app in the settings app
    * - Re-enable Notifications for Garner in settings app
      - 
      - The app can send notifications again
    * - Open Garner
      - 
      - 
        * There should be an un-actioned Reflection Reminder prompt in the Reflection List
        * The Reflection Reminder text should say the schedule for the reminder set
        * The Reflection Reminder text should no longer say the reminders are paused due to permission not being granted
        * The Reflection Reminder button should say "Update Reminder"
    * - 
        * Press "Update Reminder"
        * Set Daily Reflection Reminder schedule to trigger 2 minutes into the future
      - 
      - 
        * The Reflection Reminder text shows the schedule as daily and set to trigger at the time set
        * The Reflection Reminder button says "Update Reminder"
    * - Close app
      - 
      - The is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - At the time set a local notification is triggered that say it's time for the user to reflect on their day
  