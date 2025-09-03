==================================
User removes a reflection reminder
==================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0012
      - 
        * https://github.com/colinfwren/garner/issues/10

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
    * - Press the "Remove Reminder" button
      - 
      -
        * The Reflection Reminder sheet is dismissed
        * The Reflection Reminder text should no longer show a schedule but explain how reminders can help
        * The Reflection Reminder button says "Set Reminder"
    * - 
        * Press the "Set Reminder" button
        * Don't save the Reminder and dismiss the sheet after verifying the details
      - 
      - The Reflection Reminder sheet should be shown with the frequency set to daily and the time set to the time set before
    * - Close the app
      - 
      - The app is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - No local notification is created