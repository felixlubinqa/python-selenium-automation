#HW - 3 Revision

#1 Practice with locators


# Url = https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dap_frn_logo%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0


# Your name ---------------------------------------------------
# $$("#ap_customer_name")

# Number / Email ---------------------------------------------------
# $$("#ap_email")
# $$("input.a-input-text[name='email']")


# Password Field-----------------------------------------------
# $$("input.auth-require-password-validation")


# Password Characters----------------------------------------
# $$("#auth-password-requirement-info")


# Re-Enter Password-------------------------------------------
# $$("input.auth-require-fields-match[name=passwordCheck]")


# Continue Button ------------------------------------------------
# $$("#continue")


# Conditions of Use-------------------------------------
# $$("a[href$='=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")


# Privacy Notice--------------------------------
# $$("a[href*='ap_register_notification_privacy_notice']")


# Already have an account-----------------------------
# $$("a.a-link-emphasis")'
