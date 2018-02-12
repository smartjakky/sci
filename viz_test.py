from superset.connectors.connector_registry import ConnectorRegistry
from flask_appbuilder.security.sqla.models import User
from superset.viz import TableViz
from superset import db
from flask import g
import json


f = open('d:\\home\\pivot_viz\\form_data.json')
form_data_json = f.read()
f.close()

g.user = db.session.query(User).filter(User.id == 2).one()
form_data = json.loads(form_data_json)
datasource_type = form_data.get('viz_type', 'table')
datasource_id = form_data['datasource'].split('__')[0]
datasource = ConnectorRegistry.get_datasource(datasource_type, datasource_id, db.session)
viz = TableViz(datasource, form_data)
res = viz.get_payload(force=True)
# print(res)
with open('d:\\home\\pivot_viz\\response.json', 'w', encoding='utf8') as f:
    f.write(viz.json_dumps(res))

