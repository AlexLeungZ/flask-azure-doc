# Known Issue

## HTMX version 2.0.0+

### Issue: Class Stealing

- HTMX settling phase reverting all class added by js script
- Ref: [HTMX "steals" classes added during settle](https://github.com/bigskysoftware/htmx/issues/412)
- Ref: [Configuration Reference](https://htmx.org/reference/#config)

### Effect: JS div size not respected

- div size controlled by js script not render correctly

### Solution <!-- markdownlint-disable-line MD024 -->

- Revert to version v1.9.12
