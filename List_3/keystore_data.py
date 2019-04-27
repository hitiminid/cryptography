from dataclasses import dataclass


@dataclass
class KeyStoreData:
    path: str
    password: str
    key_identifier: str
    encryption_mode: str
