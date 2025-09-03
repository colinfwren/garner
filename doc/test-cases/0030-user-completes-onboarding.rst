================================================
User completes onboarding on first launching app
================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0030
      - 
        * https://github.com/colinfwren/garner/issues/25

====
Setup
====

- The user hasn't used the app before

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - Reset simulator or uninstall app on device
      - 
      - The app should no longer be installed on the device
    * - Install app
      - 
      - The app should be installed on the device
    * - Open App
      - 
      - The app should open to the first onboarding step - "Welcome"
    * - Press "Next" or swipe left
      - 
      - The onboarding progresses from the "Welcome" onboarding step to "Reflect"
    * - Press "Next" or swipe left
      - 
      - The onboarding progresses from the "Reflect" onboarding step to "Grow"
    * - Press "Next" or swipe left
      - 
      - 
        * The onboarding progresses from the "Grow" onboarding step to "Thrive"
        * The "Next" button changes to a "Done" button
    * - Press "Done"
      - 
      - 
        * The onboarding disappears
        * The Reflection List is shown
    * - Close the app and kill the process (swipe in task manager)
      - 
      - The app is no longer running
    * - Launch the app
      - 
      - The app opens on the Reflection List and not the Onboarding

  