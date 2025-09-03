===============================================================================================
User is shown the un-action Reflection Reminder prompt when choosing cancel on the in-app alert
===============================================================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0028
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
      - The Reflection Reminder is scheduled for 2 minutes timed
    * - Wait for the Reflection Reminder to trigger
      - 
      - The Reflection Reminder notification pops up on the device
    * - Dismiss the Reflection Reminder alert
      - 
      - 
        * The Reflection Reminder alert is dismissed
        * No new Reflection is added and the user remains on the screen they were on
    * - View the Reflection List
      - 
      - There is an un-actioned Reflection Reminder shown in the Reflection List
  