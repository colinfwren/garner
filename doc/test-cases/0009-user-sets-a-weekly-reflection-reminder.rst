=====================================
User sets a weekly reflection reminder
=====================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0009
      - 
        * https://github.com/colinfwren/garner/issues/8

====
Setup
====

- There's an existing question in the system

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - 
        * View the Settings Screen
        * Enable notifications if not already enabled
      - 
      - The Reflection Reminder button should say "Set Reminder"
    * - Set Weekly Reflection Reminder schedule to trigger on the current day and 2 minutes into the future
      - 
      - 
        * The Reflection Reminder text shows the schedule as weekly and set to trigger at the time set on the day of the week set
        * The Reflection Reminder button changes to "Update Reminder"
    * - 
        * Press the "Update Reminder" button
        * After verifying details dismiss the sheet without saving
      - 
      - The Reflection Reminder sheet should be shown with the frequency set to weekly and the time set to the time set before and the day of the week set to the day of the week set before
    * - Close app
      - 
      - The is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - At the time set a local notification is triggered that say it's time for the user to reflect on their day