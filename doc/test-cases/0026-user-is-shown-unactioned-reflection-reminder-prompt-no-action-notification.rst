======================================================================================================================
User is shown the un-action Reflection Reminder prompt when opening app after receiving but not actioning notification
======================================================================================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0026
      - 
        * https://github.com/colinfwren/garner/issues/22

====
Setup
====

- There's at least 1 question in the system
- There's a reflection reminder Setup

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - Ensure there are no un-actioned Reflection Reminder prompts in the Reflection List
      -
      -
    * - Set the Reflection Reminder schedule to trigger in 2 minutes time
      - 
      - The Reflection Reminder is scheduled for 2 minutes time
    * - Move the app to the background or quit it
      - 
      - The app is no longer in the foreground
    * - Wait for the Reflection Reminder to trigger
      - 
      - The Reflection Reminder notification pops up on the device
    * - Don’t dismiss or action the Reflection Reminder
      - 
      - The Reflection Reminder notification stays in the device Notification Center
    * -
        * Open Garner again
        * View the Reflection List
      - 
      - There is an un-actioned Reflection Reminder shown in the Reflection List
  