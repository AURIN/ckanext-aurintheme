import ckan.plugins as plugins
from pylons import app_globals
import ckan.lib.helpers as helpers


class AURINThemePluginClass(plugins.SingletonPlugin):
    """
    Setup AURIN Theme plugin.
    """
	# Declare that this class implements IConfigurer.
	# It calls implements() to declare that it implements the IConfigurer plugin interface
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IConfigurable, inherit=True)

    def update_config(self, config):
		# Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        plugins.toolkit.add_template_directory(config, 'templates')
		
		# Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        plugins.toolkit.add_public_directory(config, 'public')
