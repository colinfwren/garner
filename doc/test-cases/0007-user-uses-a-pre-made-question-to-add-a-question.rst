===============================================
User uses a pre-made question to add a question
===============================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0007
      - 
        * https://github.com/colinfwren/garner/issues/6

====
Setup
====

- There's at least 2 existing questions in the system
- There's an existing reflection in the system
- A reflection reminder has been set up

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - View the Reflection List
      - 
      - 
        * There is a Reflection in the list
        * The Reflection has a set of Questions (note them)
        * There is no prompt to add a Question in the Reflection List
        * The "Add Reflection' button is not disabled
    * - View the Settings Screen
      - 
      - 
        * The Question list contains the existing Questions
        * There is no explanation of why user needs to add a Question
        * The Reflection Reminder should be set
    * - Press "Add Question"
      - 
      -
        * The Add Question Sheet is shown
        * The text input is shown and focused
        * The pre-made questions are shown under the input
        * The "Cancel" button is shown
    * - Press a pre-made question from the list
      - 
      - 
        * The selected question is appended to the user's Question list
        * The custom question text input is cleared
    * - View the Reflection List
      - 
      - 
        * The Reflection List does not have the "Add Question" prompt
        * The existing Reflection still has the Questions that it had before adding a new Question
        * The existing Reflection does not contain the new Question
        * The Add Reflection button is not disabled (verify it's not greyed out, don't press it yet)
    * - Wait until a minute after the scheduled Reflection Reminder is due to be triggered
      - 
      - 
        * The Reflection Reminder was triggered (don't add the reflection yet)
        * There should be an un-actioned Reflection Reminder prompt in the Reflection List
    * - Add a new Reflection
      - 
      -
        * The new Reflection includes the existing questions and the newly added question
        * The Reflection List should no longer have the un-actioned Reflection Reminder prompt
    * - Export Data
      - 
      - 
        * The existing Reflection before the Question was added has the Questions that it had and not the added Question
        * The newly added Reflection has the Questions from the Question List including the added Question