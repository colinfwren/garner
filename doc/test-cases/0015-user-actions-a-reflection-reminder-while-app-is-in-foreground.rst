=============================================================
User actions a reflection reminder while app is in foreground
=============================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0015
      - 
        * https://github.com/colinfwren/garner/issues/13

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
        * View the Settings Screen
        * Enable notifications if not already enabled
        * An existing Reflection Reminder has been set
      - 
      - The Reflection Reminder button should say "Update Reminder"
    * -
        * Press "Update Reminder"
        * Set Daily Reflection Reminder schedule to trigger 2 minutes into the future
        * Save the schedule
      - 
      - 
        * The Reflection Reminder text shows the schedule as daily and set to trigger at the time set
        * The Reflection Reminder button says "Update Reminder"
    * - Press the "Update Reminder" button
      - 
      - The Reflection Reminder sheet should be shown with the frequency set to daily and the time set to the time set before
    * - Wait for the Reflection Reminder to trigger
      - 
      - At the time set an alert will popup with the options to Cancel or Add Reflection
    * - Press the "Add Reflection" button in the alert
      - 
      - The user is shown the Add Reflection Sheet
    * - Save the Reflection
      - 
      - 
        * The add reflection sheet is dismissed
        * the user is on the reflection list
        * the newly created reflection is at the top of the reflection list
        * there are no unactioned reflection reminders in the reflection list