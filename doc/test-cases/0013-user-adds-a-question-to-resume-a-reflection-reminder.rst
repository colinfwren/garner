====================================================
User adds a question to resume a reflection reminder
====================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0013
      - 
        * https://github.com/colinfwren/garner/issues/12

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
        * Set Daily Reflection Reminder schedule to trigger 5 minutes into the future
        * Save the schedule
      - 
      - 
        * The Reflection Reminder text shows the schedule as daily and set to trigger at the time set
        * The Reflection Reminder button says "Update Reminder"
    * - Delete all Questions in the Question List
      - 
      - 
        * The Reflection Reminder text should say that the reminder is daily and set to trigger at the time set
        * The Reflection Reminder text should say that reminders are paused
        * The Reflection Reminder button should be disabled
        * The Question List should show an explanation around why Questions are needed to add Reflections
        * The Reflection List should show the 'Add Question" prompt
    * - Add a new Question
      - 
      - 
        * The Question List has the Question in it
        * The Question List no longer has the explanation about why a Question is needed to add Reflections
        * The Reflection List should no longer show the "Add Question" prompt
        * The Reflection Reminder text should show the schedule for as daily and the time set
        * The Reflection Reminder text should no longer say the reminders are paused
        * The Reflection Reminder button should no longer be disabled
    * - Press the "Update Reminder" button
      - 
      - The Reflection Reminder sheet should be shown with the frequency set to daily and the time set to the time set before
    * - Close app
      - 
      - The is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - At the time set a local notification is triggered that say it’s time for the user to reflect on their day
    * - Press local notification
      - 
      - 
        * The user is navigated to the Reflection list view
        * The add reflection sheet is shown
        * The Question in the add reflection sheet is the Question that was added to resume the Reflection Reminder and not the Questions that were in the Question List before the reminders were paused