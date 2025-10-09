"""Constants for the Marstek Local API integration."""
from typing import Final

DOMAIN: Final = "marstek_local_api"

# Configuration keys
CONF_PORT: Final = "port"

# Default values
DEFAULT_PORT: Final = 30000
DEFAULT_SCAN_INTERVAL: Final = 60  # Base interval in seconds
DISCOVERY_TIMEOUT: Final = 9  # Discovery window in seconds
DISCOVERY_BROADCAST_INTERVAL: Final = 2  # Broadcast every 2 seconds during discovery

# Update intervals (in multiples of base interval)
UPDATE_INTERVAL_FAST: Final = 1  # ES, Battery status (60s)
UPDATE_INTERVAL_MEDIUM: Final = 5  # EM, PV, Mode (300s)
UPDATE_INTERVAL_SLOW: Final = 10  # Device, WiFi, BLE (600s)

# Communication timeouts
COMMAND_TIMEOUT: Final = 15  # Timeout for commands in seconds
MAX_RETRIES: Final = 3  # Maximum retries for critical commands
RETRY_DELAY: Final = 2  # Delay between retries in seconds
COMMAND_MAX_ATTEMPTS: Final = 3  # Attempts per command before giving up
COMMAND_BACKOFF_BASE: Final = 1.5  # Base delay for command retry backoff
COMMAND_BACKOFF_FACTOR: Final = 2.0  # Multiplier for successive backoff delays
COMMAND_BACKOFF_MAX: Final = 12.0  # Upper bound on backoff delay
COMMAND_BACKOFF_JITTER: Final = 0.4  # Additional random jitter for backoff
UNAVAILABLE_THRESHOLD: Final = 120  # Seconds before marking device unavailable

# Firmware version threshold for value scaling
FIRMWARE_THRESHOLD: Final = 154

# API Methods
METHOD_GET_DEVICE: Final = "Marstek.GetDevice"
METHOD_WIFI_STATUS: Final = "Wifi.GetStatus"
METHOD_BLE_STATUS: Final = "BLE.GetStatus"
METHOD_BATTERY_STATUS: Final = "Bat.GetStatus"
METHOD_PV_STATUS: Final = "PV.GetStatus"
METHOD_ES_STATUS: Final = "ES.GetStatus"
METHOD_ES_MODE: Final = "ES.GetMode"
METHOD_ES_SET_MODE: Final = "ES.SetMode"
METHOD_EM_STATUS: Final = "EM.GetStatus"

# Device models
DEVICE_MODEL_VENUS_C: Final = "VenusC"
DEVICE_MODEL_VENUS_D: Final = "VenusD"
DEVICE_MODEL_VENUS_E: Final = "VenusE"

# Operating modes
MODE_AUTO: Final = "Auto"
MODE_AI: Final = "AI"
MODE_MANUAL: Final = "Manual"
MODE_PASSIVE: Final = "Passive"

OPERATING_MODES: Final = [MODE_AUTO, MODE_AI, MODE_MANUAL, MODE_PASSIVE]

# Battery states
BATTERY_STATE_IDLE: Final = "idle"
BATTERY_STATE_CHARGING: Final = "charging"
BATTERY_STATE_DISCHARGING: Final = "discharging"

# Bluetooth states
BLE_STATE_CONNECT: Final = "connect"
BLE_STATE_DISCONNECT: Final = "disconnect"

# CT states
CT_STATE_DISCONNECTED: Final = 0
CT_STATE_CONNECTED: Final = 1

# Data keys
DATA_COORDINATOR: Final = "coordinator"
DATA_DEVICE_INFO: Final = "device_info"

# Platforms
PLATFORMS: Final = ["sensor", "binary_sensor", "select"]
