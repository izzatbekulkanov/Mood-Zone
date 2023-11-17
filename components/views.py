from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ComonentsView(TemplateView):
    pass

#  Base UI
base_ui_alerts_view = ComonentsView.as_view(template_name="components/base-ui/ui-alerts.html")
base_ui_badges_view = ComonentsView.as_view(template_name="components/base-ui/ui-badges.html")
base_ui_buttons_view = ComonentsView.as_view(template_name="components/base-ui/ui-buttons.html")
base_ui_colors_view = ComonentsView.as_view(template_name="components/base-ui/ui-colors.html")
base_ui_cards_view = ComonentsView.as_view(template_name="components/base-ui/ui-cards.html")
base_ui_carousel_view = ComonentsView.as_view(template_name="components/base-ui/ui-carousel.html")
base_ui_dropdowns_view = ComonentsView.as_view(template_name="components/base-ui/ui-dropdowns.html")
base_ui_grid_view = ComonentsView.as_view(template_name="components/base-ui/ui-grid.html")
base_ui_images_view = ComonentsView.as_view(template_name="components/base-ui/ui-images.html")
base_ui_tabs_view = ComonentsView.as_view(template_name="components/base-ui/ui-tabs.html")
base_ui_accordions_view = ComonentsView.as_view(template_name="components/base-ui/ui-accordions.html")
base_ui_modals_view = ComonentsView.as_view(template_name="components/base-ui/ui-modals.html")
base_ui_offcanvas_view = ComonentsView.as_view(template_name="components/base-ui/ui-offcanvas.html")
base_ui_placeholders_view = ComonentsView.as_view(template_name="components/base-ui/ui-placeholders.html")
base_ui_progress_view = ComonentsView.as_view(template_name="components/base-ui/ui-progress.html")
base_ui_notifications_view = ComonentsView.as_view(template_name="components/base-ui/ui-notifications.html")
base_ui_media_view = ComonentsView.as_view(template_name="components/base-ui/ui-media.html")
base_ui_embed_video_view = ComonentsView.as_view(template_name="components/base-ui/ui-embed-video.html")
base_ui_typography_view = ComonentsView.as_view(template_name="components/base-ui/ui-typography.html")
base_ui_lists_view = ComonentsView.as_view(template_name="components/base-ui/ui-lists.html")
base_ui_links_view = ComonentsView.as_view(template_name="components/base-ui/ui-links.html")
base_ui_general_view = ComonentsView.as_view(template_name="components/base-ui/ui-general.html")
base_ui_ribbons_view = ComonentsView.as_view(template_name="components/base-ui/ui-ribbons.html")
base_ui_utilities_view = ComonentsView.as_view(template_name="components/base-ui/ui-utilities.html")
# Advance UI
adance_ui_sweetalerts_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-sweetalerts.html")
adance_ui_nestable_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-nestable.html")
adance_ui_scrollbar_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-scrollbar.html")
adance_ui_animation_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-animation.html")
adance_ui_tour_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-tour.html")
adance_ui_swiper_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-swiper.html")
adance_ui_ratings_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-ratings.html")
adance_ui_highlight_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-highlight.html")
adance_ui_scrollspy_view = ComonentsView.as_view(template_name="components/advance-ui/advance-ui-scrollspy.html")
# Widgets
widgets_view=ComonentsView.as_view(template_name="components/widgets.html")
# Forms
forms_elements_view=ComonentsView.as_view(template_name="components/forms/forms-elements.html")
forms_select_view=ComonentsView.as_view(template_name="components/forms/forms-select.html")
forms_checkboxs_radios_view=ComonentsView.as_view(template_name="components/forms/forms-checkboxs-radios.html")
forms_pickers_view=ComonentsView.as_view(template_name="components/forms/forms-pickers.html")
forms_masks_view=ComonentsView.as_view(template_name="components/forms/forms-masks.html")
forms_advanced_view=ComonentsView.as_view(template_name="components/forms/forms-advanced.html")
forms_range_sliders_view=ComonentsView.as_view(template_name="components/forms/forms-range-sliders.html")
forms_validation_view=ComonentsView.as_view(template_name="components/forms/forms-validation.html")
forms_wizard_view=ComonentsView.as_view(template_name="components/forms/forms-wizard.html")
forms_editors_view=ComonentsView.as_view(template_name="components/forms/forms-editors.html")
forms_file_uploads_view=ComonentsView.as_view(template_name="components/forms/forms-file-uploads.html")
forms_layouts_view=ComonentsView.as_view(template_name="components/forms/forms-layouts.html")
forms_select2_view = ComonentsView.as_view(template_name="components/forms/forms-select2.html")
# Tables
tables_basic_view=ComonentsView.as_view(template_name="components/tables/tables-basic.html")
tables_gridjs_view=ComonentsView.as_view(template_name="components/tables/tables-gridjs.html")
tables_listjs_view=ComonentsView.as_view(template_name="components/tables/tables-listjs.html")
tables_datatables_view=ComonentsView.as_view(template_name="components/tables/tables-datatables.html")
# Charts
# Apex Charts
charts_apex_charts_line_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-line.html")
charts_apex_charts_area_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-area.html")
charts_apex_charts_column_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-column.html")
charts_apex_charts_bar_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-bar.html")
charts_apex_charts_mixed_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-mixed.html")
charts_apex_charts_timeline_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-timeline.html")
charts_apex_charts_candlestick_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-candlestick.html")
charts_apex_charts_boxplot_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-boxplot.html")
charts_apex_charts_bubble_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-bubble.html")
charts_apex_charts_scatter_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-scatter.html")
charts_apex_charts_heatmap_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-heatmap.html")
charts_apex_charts_treemap_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-treemap.html")
charts_apex_charts_pie_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-pie.html")
charts_apex_charts_radialbar_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-radialbar.html")
charts_apex_charts_radar_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-radar.html")
charts_apex_charts_polar_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-polar.html")
charts_apex_charts_funnel_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-funnel.html")
charts_apex_charts_rangearea_view=ComonentsView.as_view(template_name="components/charts/apex-charts/charts-apex-range-area.html")
# Chart JS
charts_chartjs_view=ComonentsView.as_view(template_name="components/charts/charts-chartjs.html")
# Echart
charts_echarts_view=ComonentsView.as_view(template_name="components/charts/charts-echarts.html")
# Icons
icons_remix_view=ComonentsView.as_view(template_name="components/icons/icons-remix.html")
icons_boxicons_view=ComonentsView.as_view(template_name="components/icons/icons-boxicons.html")
icons_materialdesign_view=ComonentsView.as_view(template_name="components/icons/icons-materialdesign.html")
icons_lineawesome_view=ComonentsView.as_view(template_name="components/icons/icons-lineawesome.html")
icons_feather_view=ComonentsView.as_view(template_name="components/icons/icons-feather.html")
icons_crypto_view=ComonentsView.as_view(template_name="components/icons/icons-crypto.html")
# Maps
maps_google_view=ComonentsView.as_view(template_name="components/maps/maps-google.html")
maps_vector_view=ComonentsView.as_view(template_name="components/maps/maps-vector.html")
maps_leaflet_view=ComonentsView.as_view(template_name="components/maps/maps-leaflet.html")