from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class PagesView(TemplateView):
    pass

# Authenticatin
authentication_signin_basic= PagesView.as_view(template_name="pages/authentication/auth-signin-basic.html")
authentication_signin_cover= PagesView.as_view(template_name="pages/authentication/auth-signin-cover.html")
authentication_signup_basic= PagesView.as_view(template_name="pages/authentication/auth-signup-basic.html")
authentication_signup_cover= PagesView.as_view(template_name="pages/authentication/auth-signup-cover.html")
authentication_pass_reset_basic= PagesView.as_view(template_name="pages/authentication/auth-pass-reset-basic.html")
authentication_pass_reset_cover= PagesView.as_view(template_name="pages/authentication/auth-pass-reset-cover.html")
authentication_lockscreen_basic= PagesView.as_view(template_name="pages/authentication/auth-lockscreen-basic.html")
authentication_lockscreen_cover= PagesView.as_view(template_name="pages/authentication/auth-lockscreen-cover.html")
authentication_logout_basic= PagesView.as_view(template_name="pages/authentication/auth-logout-basic.html")
authentication_logout_cover= PagesView.as_view(template_name="pages/authentication/auth-logout-cover.html")
authentication_success_msg_basic= PagesView.as_view(template_name="pages/authentication/auth-success-msg-basic.html")
authentication_success_msg_cover= PagesView.as_view(template_name="pages/authentication/auth-success-msg-cover.html")
authentication_twostep_basic= PagesView.as_view(template_name="pages/authentication/auth-twostep-basic.html")
authentication_twostep_cover= PagesView.as_view(template_name="pages/authentication/auth-twostep-cover.html")
authentication_404_basic= PagesView.as_view(template_name="pages/authentication/auth-404-basic.html")
authentication_404_cover= PagesView.as_view(template_name="pages/authentication/auth-404-cover.html")
authentication_404_alt= PagesView.as_view(template_name="pages/authentication/auth-404-alt.html")
authentication_500= PagesView.as_view(template_name="pages/authentication/auth-500.html")
authentication_auth_offline= PagesView.as_view(template_name="pages/authentication/auth-offline.html")
authentication_pass_change_basic= PagesView.as_view(template_name="pages/authentication/auth-pass-change-basic.html")
authentication_pass_change_cover= PagesView.as_view(template_name="pages/authentication/auth-pass-change-cover.html")
authentication_offline= PagesView.as_view(template_name="pages/authentication/auth-offline.html")
# Pages 
pages_starter= PagesView.as_view(template_name="pages/pages-starter.html")
pages_profile= PagesView.as_view(template_name="pages/pages-profile.html")
pages_profile_settings= PagesView.as_view(template_name="pages/pages-profile-settings.html")
pages_team= PagesView.as_view(template_name="pages/pages-team.html")
pages_timeline= PagesView.as_view(template_name="pages/pages-timeline.html")
pages_faqs= PagesView.as_view(template_name="pages/pages-faqs.html")
pages_pricing= PagesView.as_view(template_name="pages/pages-pricing.html")
pages_gallery= PagesView.as_view(template_name="pages/pages-gallery.html")
pages_maintenance= PagesView.as_view(template_name="pages/pages-maintenance.html")
pages_coming_soon= PagesView.as_view(template_name="pages/pages-coming-soon.html")
pages_sitemap= PagesView.as_view(template_name="pages/pages-sitemap.html")
pages_search_results= PagesView.as_view(template_name="pages/pages-search-results.html")

pages_landing= PagesView.as_view(template_name="pages/pages-landing.html")
pages_nft_landing = PagesView.as_view(template_name="pages/pages-nft-landing.html")
pages_job_landing = PagesView.as_view(template_name="pages/pages-job-landing.html")

pages_privacy_policy = PagesView.as_view(template_name="pages/pages-privacy-policy.html")
pages_term_conditions = PagesView.as_view(template_name="pages/pages-term-conditions.html")
