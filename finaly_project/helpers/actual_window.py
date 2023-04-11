def actual_window(browser):
    parent_guid = browser.current_window_handle
    all_guid = browser.window_handles

    for guid in all_guid:
        if guid != parent_guid:
            browser.switch_to.window(guid)
