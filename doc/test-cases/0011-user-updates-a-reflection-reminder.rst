==================================
User updates a reflection reminder
==================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0011
      - 
        * https://github.com/colinfwren/garner/issues/9

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
    * - 
        * Press the "Update Reminder" button
        * After verifying the details dismiss the sheet without saving
      - 
      - The Reflection Reminder sheet should be shown with the frequency set to daily and the time set to the time set before
    * - Close app
      - 
      - The is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - At the time set a local notification is triggered that say it's time for the user to reflect on their day
    * - Update the Reflection Reminder schedule to a weekly frequency with the weekday set to the current day of the week and the time set to 2 minutes in the fuiture
      - 
      - 
        * The Reflection Reminder text shows the schedule as weekly and set to trigger on the day of the week set at the time set
        * The Reflection Reminder button says "Update Reminder"
    * - 
        * Press the "Update Reminder" button
        * After verifying details dismiss the sheet without saving
      - 
      - The Reflection Reminder sheet should be shown with the frequency set to weekly with the day of the week set to the week day selected before and the time set to the time selected before
    * - Close app
      - 
      - The is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - At the time set a local notification is triggered that say it's time for the user to reflect on their day
    * - Update the Reflection Reminder to be a monthly reminder set to trigger on the current day of the month and the time is 2 minutes into the future
      - 
      - 
        * The Reflection Reminder text is updated to show the schedule as monthly with the day of the month being the selected day of the month and the time being the selected time
        * The Reflection Reminder button says "Update Reminder"
    * - 
        * Press the "Update Reminder" button
        * After verifying details dismiss the sheet without saving
      - 
      - The Reflection Reminder sheet shows with the frequency set to monthly, the day of the month set to the selected day of the month and then time set to the selected time
    * - Close app
      - 
      - The is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - At the time set a local notification is triggered that say it's time for the user to reflect on their day