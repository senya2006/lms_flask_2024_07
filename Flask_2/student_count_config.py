from webargs import fields, validate

student_count_config = {
    "count": fields.Int(
        missing=100,
        validate=[validate.Range(min=1, max=1000, min_inclusive=True, max_inclusive=True)],
    )
}
