from dataclasses import dataclass
from typing import Optional

from marshmallow_dataclass import class_schema
from marshmallow_dataclass.typing import Email, Url

from src.enums import CultureName, Currency


@dataclass
class Payer:
    """
    Доп. поле, куда передается информация о плательщике
    """

    FirstName: Optional[str]
    LastName: Optional[str]
    MiddleName: Optional[str]
    Birth: Optional[str]
    Street: Optional[str]
    Address: Optional[str]
    City: Optional[str]
    Country: Optional[str]
    Phone: Optional[str]
    Postcode: Optional[str]


@dataclass
class Charge:
    """
    Оплата по криптограмме, параметры запроса
    """

    # TODO докинуть валидацию, хотелось бы

    Amount: float
    Currency: Optional[Currency]
    IpAddress: str
    Token: str  # CardCryptogramPacket
    PaymentUrl: Optional[Url]
    InvoiceId: Optional[str]
    Description: Optional[str]
    Email: Email
    CultureName: Optional[CultureName]
    AccountId: str
    Email: Optional[Email]
    Payer: Optional[Payer]
    JsonData: Optional[dict]


charge_schema = class_schema(Charge)
