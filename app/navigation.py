from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

kv = """
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import MDLabel kivymd.label.MDLabel
#:import MDSeparator kivymd.cards.MDSeparator
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader

<NavDrawerIconButton@NavigationDrawerIconButton>
    on_release:
        app.screens.show_screen(root.text)

<ContentNavigationDrawer@MDNavigationDrawer>
    drawer_logo: './data/images/icon.png'
    use_logo: 'logo'
    elevation: 10

    NavDrawerIconButton:
        icon : 'view-dashboard'
        text: "Dashboard"

    NavDrawerIconButton:
        icon : 'wallet'
        text: "Expenses"

    NavDrawerIconButton:
        icon : 'star-four-points'
        text: "Items"

    NavDrawerIconButton:
        icon : 'eye-outline'
        text: "Insights"

    NavDrawerIconButton:
        icon : 'chart-pie'
        text: "Analysis"

    NavDrawerIconButton:
        icon : 'wallet-outline'
        text: "Budget"

    NavigationDrawerDivider:

    NavDrawerIconButton:
        icon : 'exit-to-app'
        text: "Exit"
        on_release:
            app.stop()

<NavigationScreen@Screen>
    name: 'NavigationScreen'
    nav_layout : nav_layout
    opacity: 0
    on_enter:
        app.screens.show_screen('Dashboard')
        root.opacity= 1
    NavigationLayout:
        id: nav_layout
        nav_drawer : nav_drawer.__self__
        toolbar : toolbar.__self__
        scrn_mgr : scrn_mgr.__self__

        ContentNavigationDrawer:
            id: nav_drawer

        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id: toolbar
                title: app.title
                md_bg_color: app.theme_cls.primary_color
                background_palette: 'Primary'
                background_hue: '500'
                elevation: 10
                left_action_items:
                    [['menu', lambda x: nav_layout.toggle_nav_drawer()]]
                right_action_items:
                    [['dots-vertical', lambda x: nav_layout.toggle_nav_drawer()]]

            ScreenManager:
                id: scrn_mgr

            Widget:
                size_hint: (None, None)
                size: (0, 0)
"""


class NavigationScreen(Screen):
    Builder.load_string(kv)

    def __init__(self, **kwargs):
        super(NavigationScreen, self).__init__(**kwargs)
        from kivy.app import App
        import os
        import shutil
        from dtclasses import init_session

        app = App.get_running_app()

        # Get correct data directory for Android and Desktop
        try:
            # Android: use app.user_data_dir which maps to internal storage
            data_dir = app.user_data_dir
        except Exception:
            data_dir = os.path.dirname(os.path.abspath(__file__))

        f_path = os.path.join(data_dir, 'extrac.db')

        # Find source db - check multiple locations
        app_dir = os.path.dirname(os.path.abspath(__file__))
        src_db = os.path.join(app_dir, 'extrac.db')

        # On Android, files are in /data/data/... - try to find it
        if not os.path.exists(src_db):
            # Try Android asset path
            possible = [
                '/data/data/org.digitalexpensetracker/files/app/extrac.db',
                os.path.join(os.path.dirname(app_dir), 'extrac.db'),
            ]
            for p in possible:
                if os.path.exists(p):
                    src_db = p
                    break

        if not os.path.exists(f_path):
            if os.path.exists(src_db):
                shutil.copyfile(src_db, f_path)
            else:
                # Create empty db if source not found
                f_path = os.path.join(data_dir, 'extrac.db')

        init_session(f_path)
