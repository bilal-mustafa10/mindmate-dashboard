from wagtail import hooks


@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels[:] = [item for item in panels if item.name != 'site_summary']


@hooks.register('construct_main_menu')
def hide_explorer_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'explorer']
    #menu_items[:] = [item for item in menu_items if item.name != 'documents']
    #menu_items[:] = [item for item in menu_items if item.name != 'images']
    menu_items[:] = [item for item in menu_items if item.name != 'videos']
    menu_items[:] = [item for item in menu_items if item.name != 'reports']
    menu_items[:] = [item for item in menu_items if item.name != 'help']


@hooks.register('construct_settings_menu')
def hide_user_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'redirects']
    menu_items[:] = [item for item in menu_items if item.name != 'sites']
    menu_items[:] = [item for item in menu_items if item.name != 'groups']
    menu_items[:] = [item for item in menu_items if item.name != 'collections']
    menu_items[:] = [item for item in menu_items if item.name != 'workflows']
    menu_items[:] = [item for item in menu_items if item.name != 'workflow_tasks']
