"""Auto-generated file, do not edit by hand. CG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CG = PhoneMetadata(id='CG', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='11\\d', possible_number_pattern='\\d{3}'),
    toll_free=PhoneNumberDesc(national_number_pattern='111', possible_number_pattern='\\d{3}', example_number='111'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11[78]', possible_number_pattern='\\d{3}', example_number='117'),
    short_code=PhoneNumberDesc(national_number_pattern='11[12678]', possible_number_pattern='\\d{3}', example_number='117'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    carrier_specific=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_data=True)
