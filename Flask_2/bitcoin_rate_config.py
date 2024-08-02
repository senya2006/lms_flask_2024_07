from webargs import fields, validate

bitcoin_rate_config = {
    "currency": fields.Str(
        missing="USD",
        validate=validate.Length(min=1)
    ),
    "convert": fields.Int(
        missing=1,
        validate=[validate.Range(min=1)]
    )
}