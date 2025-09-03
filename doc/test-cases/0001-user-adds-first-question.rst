========================
User adds First Question
========================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0001
      - 
        * https://github.com/colinfwren/garner/issues/3
        * https://github.com/colinfwren/garner/issues/18
        * https://github.com/colinfwren/garner/issues/15
        * https://github.com/colinfwren/garner/issues/24

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - View the Reflection List
      - 
      - 
        * There should be no Reflections in the reflection list
        * The reflection list should have a prompt saying there's no questions in the system and to add one
        * The "Add refleciton" button should be disabled
    * - View question list
      - 
      - 
        * Should see "add question" button and explanation of how adding a question works within app
    * - Press "Add Question" button
      - 
      - 
        * The Add Question Sheet is shown
        * The text input is shown and focused
        * The list of pre-made questions is shown below the text input
        * The "Cancel" button is shown
    * -
        * Enter Question into the input field
        * Press Add button in the sheet header
        * Verify Question was added
      - What went well this week?
      - 
        * After adding Question
        * The Question List should show the Question
        * The Question in the Question List should be have a swipe menu
        * The explanation about Questions should no longer be shown
        * The user should see a prompt to add their first update
        * The user should see the Reflection Reminder button
    * - 
        * Press the "Enable Notifications" button if not already enabled
        * Press "Set Reminder" in the Reflection Reminder section
      -
        * Frequency: daily
        * Time: 2 minutes from current time
      - 
        * The Reflection Reminder Ui is updated to show that the Reflection Reminder has been set to a daily schedule at the time set to
    * - View the Reflection List
      - 
      -
        * The "Add Question" prompt is no longer shown
        * The "Add Reflection" button is no longer disabled (verify it's not greyed out, don't press)
        * The "Add First Reflection" prompt is shown in the Reflection List
    * - Wait until a minute after the scheduled Reflection Reminder is due to be triggered
      - 
      - 
        * The Reflection Reminder is triggered (don't add the Reflection)
        * There should be an un-actioned Reflection Reminder prompt in the Reflection List
    * - Add a new Reflection
      - 
      -
        * The newly added Question is shown in the Reflection's list of questions
        * The Reflection List should no longer have the un-actioned Reflection Reminder prompt
    * - Export Data
      - 
      - 
        * The newly added Reflection should be present with the newly added Question