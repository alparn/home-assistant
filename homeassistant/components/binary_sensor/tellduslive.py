"""
Support for binary sensors using Tellstick Net.

This platform uses the Telldus Live online service.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/binary_sensor.tellduslive/

"""
import logging

from homeassistant.components import tellduslive
from homeassistant.components.binary_sensor import BinarySensorDevice
from homeassistant.components.tellduslive.entry import TelldusLiveEntity

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up Tellstick sensors."""
    if discovery_info is None:
        return
    client = hass.data[tellduslive.DOMAIN]
    add_entities(
        TelldusLiveSensor(client, binary_sensor)
        for binary_sensor in discovery_info
    )


class TelldusLiveSensor(TelldusLiveEntity, BinarySensorDevice):
    """Representation of a Tellstick sensor."""

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self.device.is_on
