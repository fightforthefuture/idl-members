Information on the installation, configuration, and design of the Internet Defense League member code.

## Installation

To install, add the following code to your page. It is asynchronous and non-blocking so it can safely be added to the ``<head>`` tag, though it can be included anywhere.

    <script type="text/javascript">
        window._idl = {};
        (function() {
            var idl = document.createElement('script');
            idl.type = 'text/javascript';
            idl.async = true;
            idl.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'members.internetdefenseleague.org/include/?url=' + (_idl.url || '') + '&campaign=' + (_idl.campaign || '') + '&variant=' + (_idl.variant || 'banner');
            document.getElementsByTagName('body')[0].appendChild(idl);
        })();
    </script>

When closed, a cookie is set to ensure that the user is not prompted with the message for the next hour.

### Customization

Users can configure the include by adding key/value properties to the ``window._idl`` object.

In addition to configuration of the JavaScript include, the values of all settings are passed to the backend as querystring parameters, so future properties can affect the content or style of the IDL message presented to the user.

Current configuration properties:

#### variant

The ``variant`` property allows the implementor to change the presentation method of the IDL message. Two variants are currently implemented:

1. ``banner``, which loads the IDL message in a banner fixed to the top of the page.
2. ``modal``, which loads the IDL message in a modal window positioned in the center of the page when first loaded.

Default: ``'banner'``

Permitted values: ``'banner'``, ``'modal'``

Example:

    _idl.variant = 'banner';


#### campaign

The ``campaign`` property defines the IDL campaign whose message should show. If set to ``null`` (the default), the latest active IDL campaign's message will be shown (if any). If set to a string campaign identifier, only messages related to that campaign will be shown (if that campaign is active).

Default: ``null``

Permitted values: ``null``, ``'name_of_campaign'``

Example:

    _idl.campaign = 'sopa';


#### url

If the implementor is dissatisfied with the presentation of the IDL message, they can specify a custom URL to be loaded by the ``<iframe />``. To prevent outdated messages from being displayed, it is recommended to use this in conjunction with the ``campaign`` property.

TODO: create styleguide for custom pages, add screenshot of example (Reddit?)

Default: ``null``

Permitted values: ``null``, ``'http://url.of/custom/message'``

Example:

    _idl.url = 'http://url.of/custom/message';


### Configured example

    <script type="text/javascript">
        window._idl = {};
        _idl.variant = 'modal';
        _idl.campaign = 'sopa';
        (function() {
            var idl = document.createElement('script');
            idl.type = 'text/javascript';
            idl.async = true;
            idl.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'members.internetdefenseleague.org/include/?url=' + (_idl.url || '') + '&campaign=' + (_idl.campaign || '') + '&variant=' + (_idl.variant || 'banner');
            document.getElementsByTagName('body')[0].appendChild(idl);
        })();
    </script>


## Implementation details

The include code does two things, behaving similarly to Google Analytics, Twitter widgets, and other prominent embed codes:

1. Creates a customization object in the page's window scope (``_idl``)
2. Creates and appends a ``<script>`` tag, which loads a JavaScript script off the IDL servers.

The ``<script>`` appended to the page parses the configuration object and does a few additional steps:

1. Creates and appends an ``<iframe>`` that hosts the IDL message
2. Includes a CSS file to ensure that the ``<iframe>`` is positioned correctly and styles
3. Ensures that users are not prompted with the IDL message more than once an hour (if configured to load in a modal window).


### External script tag

There are a number of pros and cons related to the choice to load a ``<script>`` tag (vs. having users directly include the ``<iframe>`` and CSS).


#### Pros

- Maintainability: changes can be made to the include code without asking users to change their embed code.
- Simpler installation, especially if we want to include more complex configuration
- Allows for much more complex behavior, as we can have a backend process generate the JavaScript
- Can be run asynchornously and without binding additional events, preventing it from impacting performance on member sites


#### Cons

These are all related to security, as the prominence of both IDL and its member sites makes us a potential attack vector. If a third party gains access to IDL's servers, they can:

- Change the message of the ``<iframe>`` endpoint, which coulf be immediately proliferated to all IDL member sites.
- Modify the JavaScript included into pages, giving them access to IDL members' users' cookie data, among other things. This could be used to hijack Reddit session IDs, for example, with relative ease.

Mitigation steps (aside from common security server-side security measures) to these possibilities are not immediately obvious, but might include:

- Paying a third party to monitor and manage IDL servers (watching for intrusion and ensuring that all security patches are applied, etc)
- Serving everything with SSL, whenever possible
- Encouraging IDL members to always use SSL
