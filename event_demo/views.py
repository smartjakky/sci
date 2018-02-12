from flask_appbuilder.views import BaseView, expose, expose_api


class EventView(BaseView):
    """事件通知视图类"""
    @expose('/event', methods=('GET',))
    def get_new_event_info(self):
        pass
