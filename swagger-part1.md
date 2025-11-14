---
swagger: "2.0"
info:
  description: "<h1>Metricool API</h1>\r\n        <p>The base URL for all endpoints\
    \ is: https://app.metricool.com/api</p>\r\n        <p>All endpoints require authentication.\
    \ To identify yourself properly, you must include 3 parameters in all calls</p>\r\
    \n        <p>You can add the parameters directly in the request <b>(the only parameter\
    \ that can be implemented in the header with name X-Mc-Auth is the userToken)</b></p>\r\
    \n        <ul>\r\n        <li><b>userToken:</b> It is a unique authorization code\
    \ for each user and can be found in the account settings.</li>\r\n        <li><b>userId:</b>\
    \ the user identifier of your Metricool account.</li>\r\n        <li><b>blogId:</b>\
    \ It is the identification number of the brand, this number can be easily found\
    \ from the browser url</li>\r\n        </ul>\r\n        <p>Example of a request\
    \ so that you can see the integration of the parameters in the request (this specific\
    \ request allows you to find all the brands of a certain user)</p>\r\n       \
    \ <p>https://app.metricool.com/api/admin/simpleProfiles?blogId=1234567&amp;userId=1234567&amp;userToken=GFJAFBAKFBAK32BKJBFKSABFKABKJFAKABFJKSDBFAK<p>"
  version: "2.0.0"
  title: "Metricool API"
host: "app.metricool.com"
basePath: "/api"
tags:
- name: "Admin Service"
- name: "Coupon Partner Api Service"
- name: "Customize Report Service"
- name: "Gif Explorer Service"
- name: "Linkin Bio Service"
- name: "Offline Report Service"
- name: "Payments Rest Service"
- name: "Ping Service"
- name: "Planner Service"
- name: "Profile Settings Service"
- name: "Stats Service"
- name: "TikTok WH Service"
- name: "User Settings Service"
- name: "Vendasta Rest Service"
- name: "Webhook Base Api Service"
- name: "Looker studio connector Api Service"
- name: "Data Studio Service"
- name: "Analytics Api Service"
- name: "Analytics Catalogs ApiService"
- name: "Bluesky Analytics Api Service"
- name: "Competitors Api Service"
- name: "Competitors Posts Api Service"
- name: "Facebook Analytics Service"
- name: "Gbp Analytics Service"
- name: "Hashtags Tracker Api Service"
- name: "Instagram Analytics Service"
- name: "Linkedin Analytics Service"
- name: "Media Api Service"
- name: "Pinterest Analytics Api Service"
- name: "Smart Links Api Service"
- name: "Threads Analytics Api Service"
- name: "TikTok Analytics Service"
- name: "Youtube Analytics Service"
- name: "Adgroups Api Service"
- name: "Ads Api Service"
- name: "Ads Previews Api Service"
- name: "Campaigns Service"
- name: "Facebook Ads Account Api Service"
- name: "Keywords Api Service"
- name: "Recommendations Api Service"
- name: "Suggestions Service"
- name: "Agency Customization Kit Api Service"
- name: "Agency end-clients Api Service"
- name: "Agency team members Api Service"
- name: "Agency Users Api Service"
- name: "Authorization Api Service"
- name: "Brand Role Collaborators Api Service"
- name: "Brand Roles Api Service"
- name: "Oauth Api Service"
- name: "Backoffice Agencies Rest Services"
- name: "Backoffice ICS Calendar Rest Services"
- name: "Chat Api Service"
- name: "Feature Toggle Service"
- name: "Conversations Api Service"
- name: "Inbox Notes Api Service"
- name: "Inbox Status Change Api Service"
- name: "Post Comments Api Service"
- name: "Reviews Api Service"
- name: "Ai Api Service"
- name: "Ai Natural Language Scheduling Api Service"
- name: "Canva integration service"
- name: "Drive integration service"
- name: "This endpoint returns the required configuration to embed Metricool in our\
    \ partners' sites"
- name: "Customize Report Api Service"
- name: "Report Api Service"
- name: "Approval Task Api Service"
- name: "Best Times Api Service"
- name: "Boards Api Service"
- name: "Catalogs Api Service"
- name: "Counters Api Service"
- name: "ICS Calendar Rest Services for Metricool calendar (scheduler)"
- name: "Planner Notifications ApiService"
- name: "Posts Api Service"
- name: "Scheduled Post Events Api Service"
- name: "Scheduled Post Notes Api Service"
- name: "Library Posts Notes Api Service"
- name: "Brands Api Service"
- name: "Connections V2 Api Service"
- name: "Countries Api Service"
- name: "Payment Methods Api Service"
- name: "Subscriptions Api Service"
- name: "Third Party Apps Api Service"
- name: "Timezones Api Service"
- name: "Users Api Service"
- name: "Users Sing-ups Api Service"
- name: "Whitelabel Settings Api Service"
- name: "Legal terms api"
- name: "User contract events api service"
schemes:
- "https"
paths:
  /admin/max-profiles:
    get:
      tags:
      - "Admin Service"
      summary: "Returns the maximum number of brands for the authenticated user."
      description: ""
      operationId: "getMaxProfiles"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "integer"
            format: "int32"
  /admin/other-free-connections:
    delete:
      tags:
      - "Admin Service"
      operationId: "deleteOtherFreeConnections"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "boolean"
  /admin/simpleProfiles:
    get:
      tags:
      - "Admin Service"
      summary: "Returns the list of brands of your Metricool account."
      description: ""
      operationId: "getSimpleProfiles"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/PublicBlog"
  /admin/profiles-auth:
    get:
      tags:
      - "Admin Service"
      summary: "Returns the list of brands of your Metricool account."
      description: ""
      operationId: "getAuthenticatedProfiles"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/PublicBlog"
  /admin/detectwebsite:
    get:
      tags:
      - "Admin Service"
      operationId: "detectWebsite"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/PublicBlog"
  /admin/update-label-blog:
    get:
      tags:
      - "Admin Service"
      summary: "Updates the brand label."
      description: ""
      operationId: "updateLabelBlog"
      produces:
      - "application/json"
      parameters:
      - name: "newName"
        in: "query"
        description: "Profile name"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /admin/report-logo:
    get:
      tags:
      - "Admin Service"
      summary: "Returns the report logo URL"
      description: ""
      operationId: "getUserReportLogo"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /admin/add-profile:
    get:
      tags:
      - "Admin Service"
      summary: "Creates new profile"
      description: ""
      operationId: "addProfile"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/PublicBlog"
  /admin/delete-profile:
    get:
      tags:
      - "Admin Service"
      summary: "Remove current brand"
      description: ""
      operationId: "deleteProfile"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /admin/restore-profile:
    get:
      tags:
      - "Admin Service"
      summary: "Restore a deleted brand"
      description: ""
      operationId: "restoreProfile"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /admin/profile/setproperty:
    get:
      tags:
      - "Admin Service"
      summary: "Update brand property value"
      description: ""
      operationId: "setProfileProperty"
      produces:
      - "application/json"
      parameters:
      - name: "name"
        in: "query"
        description: "property name"
        required: false
        type: "string"
      - name: "value"
        in: "query"
        description: "property value"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /admin/profile/getproperty:
    get:
      tags:
      - "Admin Service"
      summary: "Get brand property value"
      description: ""
      operationId: "getProfileProperty"
      produces:
      - "application/json"
      parameters:
      - name: "name"
        in: "query"
        description: "property name"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /admin/blog/profiles:
    get:
      tags:
      - "Admin Service"
      summary: "Returns a brand picture of your Metricool account."
      description: ""
      operationId: "getBlogProfiles"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /admin/security/migration:
    get:
      tags:
      - "Admin Service"
      operationId: "migrateAuthentication"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "integer"
            format: "int64"
  /partner/stackCoupon:
    put:
      tags:
      - "Coupon Partner Api Service"
      operationId: "addNewCoupon"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          type: "string"
      responses:
        default:
          description: "successful operation"
  /stats/report/updatereportlogo:
    post:
      tags:
      - "Customize Report Service"
      summary: "Save new logo to be included in the report when no template is selected."
      description: ""
      operationId: "saveReportLogo"
      parameters: []
      responses:
        default:
          description: "successful operation"
  /stats/report/deletepicture:
    get:
      tags:
      - "Customize Report Service"
      summary: "Deletes the report picture logo."
      description: ""
      operationId: "deleteReportPicture"
      produces:
      - "text/plain"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /stats/report/savetemplate:
    post:
      tags:
      - "Customize Report Service"
      summary: "Saves the report template."
      description: ""
      operationId: "saveReportTemplateParam"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /stats/report/deletetemplate:
    get:
      tags:
      - "Customize Report Service"
      summary: "Delete template and update delete value to 1."
      description: ""
      operationId: "deleteTemplateUser"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/report/duplicatetemplate:
    get:
      tags:
      - "Customize Report Service"
      summary: "Duplicate a template with another name."
      description: ""
      operationId: "duplicateTemplateUser"
      produces:
      - "application/json"
      parameters:
      - name: "templateId"
        in: "query"
        description: "The id of the template you want to duplicate"
        required: false
        type: "string"
      - name: "templateName"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/TemplateReport"
  /stats/report/reporttemplateName:
    get:
      tags:
      - "Customize Report Service"
      summary: "Returns all report templates of a user."
      description: ""
      operationId: "getReportTemplateUser"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TemplateReport"
  /stats/report/reporttemplateparam:
    get:
      tags:
      - "Customize Report Service"
      summary: "Returns all parameters of a specific template"
      description: ""
      operationId: "getReportTemplateParam"
      produces:
      - "application/json"
      parameters:
      - name: "templateId"
        in: "query"
        description: "report template id"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "string"
  /stats/report/template/default-resources:
    get:
      tags:
      - "Customize Report Service"
      operationId: "getDefaultTemplateResources"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "object"
            additionalProperties:
              type: "string"
  /gifs/search:
    get:
      tags:
      - "Gif Explorer Service"
      summary: "Search gifs. When query is blank returns trendings"
      description: ""
      operationId: "search"
      produces:
      - "application/json"
      parameters:
      - name: "q"
        in: "query"
        description: "Term to search"
        required: false
        type: "string"
      - name: "offset"
        in: "query"
        description: "Offset to implement navigation"
        required: true
        type: "integer"
        format: "int32"
      - name: "limit"
        in: "query"
        description: "Max number of images to return"
        required: false
        type: "integer"
        default: 10
        minimum: 1
        format: "int32"
      - name: "lang"
        in: "query"
        description: "language for regional content; use a 2-letter ISO 639-1 language\
          \ code. By default, your metricool account language will"
        required: false
        type: "string"
      - name: "rating"
        in: "query"
        description: "rating GIF and Sticker library is thoroughly moderated and organized\
          \ by rating. By default g is used \r\n g: Contains images that are broadly\
          \ accepted as appropriate and commonly witnessed by people in a public environment.\
          \ \r\n pg: Contains images that are commonly witnessed in a public environment,\
          \ but not as broadly accepted as appropriate. \r\n pg-13: Contains images\
          \ that are typically not seen unless sought out, but still commonly witnessed\
          \ \r\n r:Contains images that are typically not seen unless sought out and\
          \ could be considered alarming if witnessed"
        required: false
        type: "string"
        default: "g"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/SearchResponse"
  /linkinbio/instagram/updateButtonPosition:
    get:
      tags:
      - "Linkin Bio Service"
      summary: "Delete item from Instagram BIO link"
      description: ""
      operationId: "updateButtonPosition"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to delete"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramLinkTree"
  /linkinbio/instagram/editcatalogitem:
    get:
      tags:
      - "Linkin Bio Service"
      summary: "Delete item from Instagram BIO link"
      description: ""
      operationId: "editCatalogItem"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to update"
        required: false
        type: "integer"
      - name: "link"
        in: "query"
        description: "new link URL"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramBioCatalog"
  /linkinbio/instagram/editcatalogbutton:
    get:
      tags:
      - "Linkin Bio Service"
      summary: "Update button link and text in Instagram BIO link"
      description: ""
      operationId: "editCatalogButton"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to update"
        required: false
        type: "integer"
      - name: "link"
        in: "query"
        description: "new link URL"
        required: false
        type: "string"
      - name: "text"
        in: "query"
        description: "new text description"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramLinkTree"
  /linkinbio/instagram/addcatalogitems:
    post:
      tags:
      - "Linkin Bio Service"
      summary: "Add one or more pictures to Instagram BIO link"
      description: ""
      operationId: "addCatalogItems"
      produces:
      - "application/json"
      parameters:
      - name: "picture"
        in: "query"
        description: "The most recent post Id (only for Instagram personal accounts)"
        required: false
        type: "string"
      - name: "igid"
        in: "query"
        description: "Instagram post identifier"
        required: false
        type: "string"
      - name: "timestamp"
        in: "query"
        description: "Unix timestamp in milis"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramBioCatalog"
  /linkinbio/instagram/addcatalogButton:
    get:
      tags:
      - "Linkin Bio Service"
      summary: "Add button to Instagram BIO link"
      description: ""
      operationId: "addCatalogButton"
      produces:
      - "application/json"
      parameters:
      - name: "textButton"
        in: "query"
        description: "button text"
        required: false
        type: "string"
      - name: "link"
        in: "query"
        description: "button Link"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramLinkTree"
  /linkinbio/instagram/getbiocatalog:
    get:
      tags:
      - "Linkin Bio Service"
      summary: "Returns Instagram BIO link contents"
      description: ""
      operationId: "getInstagramBioCatalog"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramBioCatalog"
  /linkinbio/instagram/getbioButtons:
    get:
      tags:
      - "Linkin Bio Service"
      summary: "Returns Instagram BIO link contents"
      description: ""
      operationId: "getInstagramButtonsBioCatalog"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramLinkTree"
  /linkinbio/instagram/deletecatalogimage:
    delete:
      tags:
      - "Linkin Bio Service"
      summary: "Delete item from Instagram BIO link"
      description: ""
      operationId: "deleteCatalogImage"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to delete"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramBioCatalog"
  /linkinbio/instagram/deletecatalogitem:
    delete:
      tags:
      - "Linkin Bio Service"
      summary: "Delete item from Instagram BIO link"
      description: ""
      operationId: "deleteCatalogItem"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to delete"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramLinkTree"
  /mtr/ping:
    get:
      tags:
      - "Ping Service"
      operationId: "pong"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "string"
  /actions/setTimeZone:
    get:
      tags:
      - "Planner Service"
      summary: "Define the user timezone."
      description: ""
      operationId: "setTimeZone"
      produces:
      - "application/json"
      parameters:
      - name: "timezone"
        in: "query"
        description: "time zone --> Europe/Berlin or Europe/Paris "
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /actions/normalize/image/url:
    get:
      tags:
      - "Planner Service"
      summary: "Validates that the URL is publicly accessible and transforms it into\
        \ a URL from a metricool repository"
      description: ""
      operationId: "getNormalizedImageUrl"
      produces:
      - "text/plain"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /actions/instagram/required-scopes-to-post:
    get:
      tags:
      - "Planner Service"
      operationId: "requiredInstagramScopesToPublish"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              type: "string"
  /actions/instagram/auto-candidate-posts-count-for-automation:
    get:
      tags:
      - "Planner Service"
      operationId: "getCandidatePostCountForAutomation"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "integer"
            format: "int32"
  /actions/instagram/auto-candidate-posts-for-automation:
    post:
      tags:
      - "Planner Service"
      operationId: "setCandidatePostForAutomation"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "integer"
            format: "int32"
  /actions/facebook/search-location:
    get:
      tags:
      - "Planner Service"
      operationId: "getLocations"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              $ref: "#/definitions/FacebookLocation"
  /actions/twitter/suggestions:
    get:
      tags:
      - "Planner Service"
      summary: "Returns a list of suggestions of twitter accounts."
      description: ""
      operationId: "getTwitterSuggestions"
      produces:
      - "application/json"
      parameters:
      - name: "q"
        in: "query"
        description: "Text entered in the search field"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitterEvent"
  /actions/bluesky/suggestions:
    get:
      tags:
      - "Planner Service"
      summary: "Returns a list of suggestions of Bluesky accounts."
      description: ""
      operationId: "getBlueskySuggestions"
      produces:
      - "application/json"
      parameters:
      - name: "q"
        in: "query"
        description: "Text entered in the search field"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitterEvent"
  /actions/facebook/suggestions:
    get:
      tags:
      - "Planner Service"
      summary: "Returns a list of suggestions of facebook accounts."
      description: ""
      operationId: "getFacebookSuggestions"
      produces:
      - "application/json"
      parameters:
      - name: "q"
        in: "query"
        description: "Text entered in the search field"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitterEvent"
  /actions/instagram/suggestions/hashtags:
    get:
      tags:
      - "Planner Service"
      summary: "Returns a list of suggestions of instagram hashtags."
      description: ""
      operationId: "getInstagramHashtagsSuggestions"
      produces:
      - "application/json"
      parameters:
      - name: "q"
        in: "query"
        description: "Text entered in the search field"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int32"
  /actions/linkedin/suggestions:
    get:
      tags:
      - "Planner Service"
      summary: "Returns a list of suggestions of linkedIn companies."
      description: ""
      operationId: "getLinkedInSuggestions"
      produces:
      - "application/json"
      parameters:
      - name: "q"
        in: "query"
        description: "Text entered in the search field"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitterEvent"
  /actions/csv/table:
    post:
      tags:
      - "Planner Service"
      operationId: "getCSVTable"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              $ref: "#/definitions/CalendarCSVRow"
  /profile/report/sections:
    get:
      tags:
      - "Profile Settings Service"
      operationId: "getUserReportSections"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/UserSettingsReportSections"
  /profile/lastsyncs:
    get:
      tags:
      - "Profile Settings Service"
      operationId: "getLastSyncs"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int64"
  /profile/subscription:
    get:
      tags:
      - "Profile Settings Service"
      operationId: "getUserSubscription"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/Subscription"
  /profile/timezone:
    post:
      tags:
      - "Profile Settings Service"
      operationId: "setBrandTimezone"
      parameters: []
      responses:
        default:
          description: "successful operation"
  /stats/timeline/{metric}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns time serie values for a concrete metric during a period of\
        \ time"
      description: ""
      operationId: "getTimeLine"
      produces:
      - "application/json"
      parameters:
      - name: "metric"
        in: "path"
        description: "Supported values: \r\n     For Website: Visitors, PageViews,\
          \ SessionsCount \r\n     For Blog: DailyComments, DailyPosts \r\n     For\
          \ Twitter: twitterFollowers, twTweets, 2ndLevelFollowers, LastDayActiveFollowers,\
          \ LastMonthActiveFollowers, twFavorites, twFriends, twListed, twMentions,\
          \ twRetweets, follows, unfollows\r\n     For Facebook pages: facebookLikes,\
          \ fbPosts, dailyImpressions, dailyImpressionsUnique, dailyReactions, dailyClicks,\
          \ dailyShares, dailyComments, pageImpressions, pageViews, fbFollows, fbUnfollows,\
          \ ctaClicks, callPhoneClicks, getDirectionsClicks, \r\n     For Facebook\
          \ groups: fb_group_members, fb_group_members_req, fbGroupsPosts, fbGroupsEngagement,\
          \ fbGroupsInteractions, fbGroupsReactions, fbGroupsComments\r\n     For\
          \ Instagram: igFollowers, igFollowing, igDeltaFollowers, igPosts, igLikes,\
          \ igComments, igEngagement, igSaved, igInteractions, igimpressions, igreach,\
          \ igprofile_views, igwebsite_clicks, igPostsImpressions, igPostsReach, igStoriesImpressions,\
          \ igStoriesReach, igStoriesCount\r\n     For LinkedIn: inFollowers, inPaidFollowers,\
          \ inCompanyImpressions, inPosts, inCliks, inPostsLikes, inComments\r\n \
          \    For Facebook Ads: clicks, total_action_value, cpc, cpm, cpp, ctr, impressions,\
          \ reach, spend, unique_clicks, unique_ctr\r\n     For Youtube: ytviewerPercentage,\
          \ yttotalComments, yttotalViews, yttotalVideos, yttotalSubscribers, yttotalLikes,\
          \ yttotalDislikes, yttotalFavorites, ytsubscribersGained, ytsubscribersLost,\
          \ ytviews, ytestimatedRevenue, ytestimatedMinutesWatched, ytaverageViewDuration,\
          \ ytlikes, ytdislikes, ytcomments, ytshares, ytestimatedRedPartnerRevenue,\
          \ ytadImpressions, ytmonetizedPlaybacks"
        required: true
        type: "string"
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              type: "array"
              items:
                type: "string"
  /stats/aggregation/{metric}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Engagement metric aggregated value for a period of time"
      description: ""
      operationId: "getAggregation"
      produces:
      - "application/json"
      parameters:
      - name: "metric"
        in: "path"
        description: "Supported values: igEngagement, affiliationEarned, fbPostsReach,\
          \ igPostsReach, igStoriesReach, fbDailyEngagement and pinterestEngagement"
        required: true
        type: "string"
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "igcompetitorid"
        in: "query"
        description: "(Optional) to get Instagram engagement for a competitor"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "number"
            format: "double"
  /stats/aggregations/{category}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns a list of metrics agregated for a period of time filtered\
        \ by category"
      description: ""
      operationId: "getAggregations"
      produces:
      - "application/json"
      parameters:
      - name: "category"
        in: "path"
        description: "Supported values: fbAdsPerformance, adwordsPerformance, BestTimeTweet,\
          \ FacebookAds, Facebook, Linkedin, Contents, instagram, Twitter, BestTimeIG,\
          \ Audience"
        required: true
        type: "string"
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "campaignid"
        in: "query"
        description: "(Optional) Only for fbAdsPerformance, adwordsPerformance"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "number"
              format: "double"
  /stats/values/{category}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns metrics values for a concrete day and filtered by category"
      description: ""
      operationId: "getValues"
      produces:
      - "application/json"
      parameters:
      - name: "category"
        in: "path"
        description: "Supported values: fbAdsPerformance, adwordsPerformance, BestTimeTweet,\
          \ FacebookAds, Facebook, Linkedin, Contents, instagram, Twitter, BestTimeIG,\
          \ Audience"
        required: true
        type: "string"
      - name: "date"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int32"
  /stats/twitter/posts:
    get:
      tags:
      - "Stats Service"
      summary: "Returns tweets list with metrics for the period"
      description: ""
      operationId: "getTweets"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (created, favorites, retweets, linkClicks)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/Tweet"
  /stats/posts:
    get:
      tags:
      - "Stats Service"
      summary: "Returns website posts published during the period"
      description: ""
      operationId: "getPosts"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/PublicPost"
  /stats/distribution/{type}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns website visits distribution during the period"
      description: ""
      operationId: "getGeoDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "type"
        in: "path"
        description: "Supported values: country, referers, sources"
        required: true
        type: "string"
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int64"
  /stats/twEvents/{type}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns twitter account that start following and stop following during\
        \ the period"
      description: ""
      operationId: "getTwitterEvents"
      produces:
      - "application/json"
      parameters:
      - name: "type"
        in: "path"
        description: "Supported values: follows, unfollows"
        required: true
        type: "string"
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitterEvent"
  /stats/rt/values:
    get:
      tags:
      - "Stats Service"
      summary: "Returns page views, visits and visitors for today for the website\
        \ and people reading right now"
      description: ""
      operationId: "getRTValues"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int32"
  /stats/rt/pvperhour:
    get:
      tags:
      - "Stats Service"
      summary: "Returns page views per hour distribution for a website in real time"
      description: ""
      operationId: "getRTPageViewsPerHour"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int64"
  /stats/rt/sessions:
    get:
      tags:
      - "Stats Service"
      summary: "Returns real time visit list for a website"
      description: ""
      operationId: "getRTSessions"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/VisitorSessionList"
  /stats/rt/distribution/{type}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns real time visits distribution for the website"
      description: ""
      operationId: "getRTDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "type"
        in: "path"
        description: "Values: referers, countries, sources, currentpageviews"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int64"
  /stats/rt/twitter/tweets/{type}:
    get:
      tags:
      - "Stats Service"
      operationId: "getLastTweets"
      produces:
      - "application/json"
      parameters:
      - name: "screenname"
        in: "query"
        required: false
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "from"
        in: "query"
        required: false
        type: "string"
      - name: "type"
        in: "path"
        description: "Supported values: tweets, mentions"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              $ref: "#/definitions/Tweet"
  /stats/rt/twitterProfile:
    get:
      tags:
      - "Stats Service"
      operationId: "getTwitterProfile"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/TwitterProfile"
  /stats/instagram/posts:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Instagram post list with metrics for the period"
      description: ""
      operationId: "statsServiceGetInstagramPosts"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (published, likes, comments, filter, engagement,\
          \ interactions, clicks, type, owner, impressions, reach, saved, videoviews)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramPost"
      deprecated: true
  /stats/instagram/reels:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Instagram reel list with metrics for the period"
      description: ""
      operationId: "statsServiceGetInstagramReels"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (published, likes, comments, filter, engagement,\
          \ interactions, clicks, type, owner, impressions, reach, saved, videoviews)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramReel"
  /stats/instagram/stories:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Instagram stories list with metrics for the period"
      description: ""
      operationId: "statsServiceGetInstagramStories"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (published, exits, impressions, reach, replies,\
          \ tapsForward, tapsBack)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramStory"
  /stats/{provider}/posts/types:
    get:
      tags:
      - "Stats Service"
      summary: "Returns tweets grouped by type"
      description: ""
      operationId: "getTweetsTypes"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Social media network (twitter, facebook, instagram...)"
        required: true
        type: "string"
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int32"
      deprecated: true
  /stats/gender/{provider}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns followers distribution by gender"
      description: ""
      operationId: "getComunityGenderDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: facebook, instagram"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              $ref: "#/definitions/Number"
  /stats/gender-age/{provider}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns followers distribution by gender and age"
      description: ""
      operationId: "getComunityGenderAgeDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: facebook, instagram"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/GenderAgeDistribution"
  /stats/trafficsource/{provider}:
    get:
      tags:
      - "Stats Service"
      operationId: "getCommunityTrafficSourceDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int32"
  /stats/twitch/videos:
    get:
      tags:
      - "Stats Service"
      summary: "Returns twitch videos with metrics for the period"
      description: ""
      operationId: "getTwitchVideos"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (created)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitchVideo"
  /stats/twitch/clips:
    get:
      tags:
      - "Stats Service"
      summary: "Returns twitch clips from a specific video"
      description: ""
      operationId: "getTwitchClips"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (created)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitchClip"
  /stats/twitch/video/clips:
    get:
      tags:
      - "Stats Service"
      summary: "Returns  clips from a twitch channel"
      description: ""
      operationId: "getTwitchClipsByVideo"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (created)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitchClip"
  /stats/twitch/subscriptions:
    get:
      tags:
      - "Stats Service"
      summary: "Returns  subscriptions twitch channel"
      description: ""
      operationId: "getTwitchSubscriptions"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (date)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TwitchSubscription"
  /stats/twitch/subscriptions/doughnut:
    get:
      tags:
      - "Stats Service"
      summary: "Returns subscribers distribution by type"
      description: ""
      operationId: "getSubscriptionsDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              $ref: "#/definitions/Number"
  /stats/tiktokads/campaigns:
    get:
      tags:
      - "Stats Service"
      summary: "Returns TikTok campaigns with metrics for the period"
      description: ""
      operationId: "getTikTokCampaigns"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/AdCampaign"
  /stats/age/{provider}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns followers distribution by age"
      description: ""
      operationId: "getComunityAgeDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: facebook, instagram"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              $ref: "#/definitions/Number"
  /stats/postmessage/{provider}:
    get:
      tags:
      - "Stats Service"
      summary: "Post a a message or a comment in response to anothere"
      description: ""
      operationId: "getPostMessage"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: fbMessenger, fbComments, igComments, twitterDM"
        required: true
        type: "string"
      - name: "conversationid"
        in: "query"
        description: "Message or comment to respond"
        required: false
        type: "string"
      - name: "text"
        in: "query"
        description: "Text to publish"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /stats/deletecomment/{provider}:
    get:
      tags:
      - "Stats Service"
      summary: "Delete a Facebook comment"
      description: ""
      operationId: "getDeleteComment"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: fbComments"
        required: true
        type: "string"
      - name: "commentid"
        in: "query"
        description: "Facebook comment id"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/postlike/{provider}:
    get:
      tags:
      - "Stats Service"
      summary: "Switch like (like or unlike) a Facebook comment"
      description: ""
      operationId: "getPostLike"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: fbComments"
        required: true
        type: "string"
      - name: "objectid"
        in: "query"
        description: "Facebook comment id"
        required: false
        type: "string"
      - name: "isLiked"
        in: "query"
        description: "true, if you want to remove the like"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/country/{provider}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns followers distribution by country"
      description: ""
      operationId: "getComunityCountryDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: facebook, instagram, tiktok, youtube"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              $ref: "#/definitions/Number"
  /stats/city/{provider}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns followers distribution by city"
      description: ""
      operationId: "getComunityCityDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "Supported values: facebook, instagram"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              $ref: "#/definitions/Number"
  /stats/twitter/follow:
    get:
      tags:
      - "Stats Service"
      summary: "Follow twitter account"
      description: ""
      operationId: "followTwitter"
      produces:
      - "application/json"
      parameters:
      - name: "userid"
        in: "query"
        description: "twitter user id"
        required: false
        type: "string"
      - name: "screenname"
        in: "query"
        description: "twitter screen name"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/twitter/unfollow:
    get:
      tags:
      - "Stats Service"
      summary: "Unfollow twitter account"
      description: ""
      operationId: "unfollowTwitter"
      produces:
      - "application/json"
      parameters:
      - name: "userid"
        in: "query"
        description: "twitter user id"
        required: false
        type: "string"
      - name: "screenname"
        in: "query"
        description: "twitter screen name"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/facebook/posts:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Facebook page posts list with metrics for the period"
      description: ""
      operationId: "statsServiceGetFacebookPosts"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (reactions, engagement, shares, impressions,\
          \ impressionsUnique, clicks, linkclicks, comments, videoViews, videoTimeWatched)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/FacebookPost"
  /stats/fbgroup/posts:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Facebook group posts list with metrics for the period"
      description: ""
      operationId: "getFacebookGroupPosts"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (reactions, engagement, comments)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/FacebookPost"
  /stats/linkedin/posts:
    get:
      tags:
      - "Stats Service"
      summary: "Returns LinkedIn posts list with metrics for the period"
      description: ""
      operationId: "getLinkedinPosts"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "string"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (likes, clicks, impressions, engagement, comments)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/LinkedinPost"
  /stats/linkedin/stories:
    get:
      tags:
      - "Stats Service"
      summary: "Returns LinkedIn stories list with metrics for the period"
      description: ""
      operationId: "getLinkedinStories"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (likes, clicks, impressions, engagement, comments)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/LinkedinPost"
  /stats/facebookads/campaigns:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Facebook Ads campaigns list with metrics for the period"
      description: ""
      operationId: "getFacebookAdsCampaings"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (name, objective, created, updated, impressions,\
          \ reach, conversions, clicks, start, cpm, cpc, ctr, spent)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/AdCampaign"
  /stats/adwords/campaigns:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Google Ads campaigns list with metrics for the period"
      description: ""
      operationId: "getAdwordsCampaings"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (impressions, start, cpm, cpc, ctr, cost)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/AdCampaign"
  /stats/adwords/keywords:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Google Ads keywords list with metrics for the period"
      description: ""
      operationId: "getAdwordsKeywords"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (impressions, start, cpm, cpc, ctr, cost)"
        required: false
        type: "string"
      - name: "CAMPAIGN"
        in: "query"
        description: "(optional) campaign identifier to filter"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/AdsKeyword"
  /stats/ads:
    get:
      tags:
      - "Stats Service"
      operationId: "getAdwordsAds"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              $ref: "#/definitions/Ad"
  /stats/facebookads/metricvalue:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Facebook Ads metric value"
      description: ""
      operationId: "getFacebookAdsMetricValue"
      produces:
      - "application/json"
      parameters:
      - name: "metric"
        in: "query"
        description: "metric name"
        required: false
        type: "string"
      - name: "start"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "Format: YYYYMMDD"
        required: false
        type: "integer"
      - name: "timezone"
        in: "query"
        description: "timezone to use for the date range"
        required: false
        type: "string"
      - name: "idCampaign"
        in: "query"
        description: "(optional) only to filter for a campaign"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "number"
            format: "double"
  /stats/link/distribution/{type}:
    get:
      tags:
      - "Stats Service"
      operationId: "getLinkDistribution"
      produces:
      - "application/json"
      parameters:
      - name: "type"
        in: "path"
        description: "supported values: twFollowers, facebook, instagram"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "object"
            additionalProperties:
              type: "integer"
              format: "int64"
  /stats/instagram/getbiocatalog:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Instagram BIO link contents (catalog)"
      description: ""
      operationId: "statsServiceGetInstagramBioCatalog"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramBioCatalog"
  /stats/instagram/getbioButtons:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Instagram BIO link contents"
      description: ""
      operationId: "statsServiceGetInstagramButtonsBioCatalog"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/InstagramLinkTree"
  /stats/instagram/deletecatalogitem:
    get:
      tags:
      - "Stats Service"
      summary: "Delete item from Instagram BIO link"
      description: ""
      operationId: "statsServiceDeleteCatalogItem"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to delete"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/instagram/updateButtonPosition:
    get:
      tags:
      - "Stats Service"
      summary: "Delete item from Instagram BIO link"
      description: ""
      operationId: "statsServiceUpdateButtonPosition"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to delete"
        required: false
        type: "integer"
      - name: "itemposition"
        in: "query"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/instagram/editcatalogitem:
    get:
      tags:
      - "Stats Service"
      summary: "Update picture link in Instagram BIO link"
      description: ""
      operationId: "statsServiceEditCatalogItem"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to update"
        required: false
        type: "integer"
      - name: "link"
        in: "query"
        description: "new link URL"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/instagram/editcatalogbutton:
    get:
      tags:
      - "Stats Service"
      summary: "Update button link and text in Instagram BIO link"
      description: ""
      operationId: "statsServiceEditCatalogButton"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to update"
        required: false
        type: "integer"
      - name: "link"
        in: "query"
        description: "new link URL"
        required: false
        type: "string"
      - name: "textButton"
        in: "query"
        description: "new link URL"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/instagram/editcoloritem:
    get:
      tags:
      - "Stats Service"
      summary: "Update button color in Instagram BIO link"
      description: ""
      operationId: "editColorItem"
      produces:
      - "application/json"
      parameters:
      - name: "itemid"
        in: "query"
        description: "item id to update"
        required: false
        type: "integer"
      - name: "link"
        in: "query"
        description: "new link URL"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/instagram/addcatalogitem:
    get:
      tags:
      - "Stats Service"
      summary: "Add picture to Instagram BIO link"
      description: ""
      operationId: "addCatalogItem"
      produces:
      - "application/json"
      parameters:
      - name: "picture"
        in: "query"
        description: "The most recent post Id (only for Instagram personal accounts)e"
        required: false
        type: "string"
      - name: "igid"
        in: "query"
        description: "Instagram post identifier"
        required: false
        type: "string"
      - name: "timestamp"
        in: "query"
        description: "Unix timestamp in milis"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/instagram/addcatalogButton:
    get:
      tags:
      - "Stats Service"
      summary: "Add button to Instagram BIO link"
      description: ""
      operationId: "statsServiceAddCatalogButton"
      produces:
      - "application/json"
      parameters:
      - name: "igid"
        in: "query"
        description: "button text"
        required: false
        type: "string"
      - name: "link"
        in: "query"
        description: "button Link"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "boolean"
  /stats/facebook/boost/{postId}:
    get:
      tags:
      - "Stats Service"
      summary: "Creates a paid campaign for a published Facebook post"
      description: ""
      operationId: "boostFacebookPost"
      produces:
      - "application/json"
      parameters:
      - name: "postId"
        in: "path"
        description: "published Facebook post id (Facebook identifier)"
        required: true
        type: "string"
      - name: "budget"
        in: "query"
        description: "new budget to boost"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /stats/facebook/boost/pending/{postId}:
    get:
      tags:
      - "Stats Service"
      summary: "Add the boost budget for a programmed Facebook post for first time."
      description: ""
      operationId: "boostFacebookPostPending"
      produces:
      - "application/json"
      parameters:
      - name: "postId"
        in: "path"
        description: "published Facebook post id (Facebook identifier)"
        required: true
        type: "string"
      - name: "budget"
        in: "query"
        description: "new budget to boost"
        required: false
        type: "integer"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /stats/facebook/getvalue:
    get:
      tags:
      - "Stats Service"
      summary: "Returns the boost budget for a programmed Facebook post."
      description: ""
      operationId: "boostFacebookGetValue"
      produces:
      - "application/json"
      parameters:
      - name: "postId"
        in: "query"
        description: "published Facebook post id (Facebook identifier)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "string"
  /stats/gmb/review:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Gmb review list with metrics for the period"
      description: ""
      operationId: "getGmbReviews"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (created, saves, comments)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/GmbReview"
  /stats/gmb/reviewbyid:
    get:
      tags:
      - "Stats Service"
      summary: "Returns a GMB review  from API"
      description: ""
      operationId: "getGmbReview"
      produces:
      - "application/json"
      parameters:
      - name: "reviewname"
        in: "query"
        description: "id of a review"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/GmbReview"
  /stats/gmb/media/{type}:
    get:
      tags:
      - "Stats Service"
      summary: "Returns Gmb review list with metrics for the period"
      description: ""
      operationId: "getGmbMedia"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "period start (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "end"
        in: "query"
        description: "period end (YYYYMMDD)"
        required: false
        type: "integer"
      - name: "sortcolumn"
        in: "query"
        description: "column to sort (created, saves, comments)"
        required: false
        type: "string"
      - name: "type"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/GmbMedia"
  /stats/gmb/review/reply:
    get:
      tags:
      - "Stats Service"
      summary: "Reply a GMB review"
      description: ""
      operationId: "replyReview"
      produces:
      - "application/json"
      parameters:
      - name: "reviewname"
        in: "query"
        description: "id of a review (String)"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: " text of a review (String)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "object"
            additionalProperties:
              type: "object"
  /stats/gmb/review/reply/remove:
    get:
      tags:
      - "Stats Service"
      summary: "Deletes a GMB review reply"
      description: ""
      operationId: "deleteReplyReview"
      produces:
      - "application/json"
      parameters:
      - name: "reviewname"
        in: "query"
        description: "id of a review (String)"
        required: false
        type: "string"
      responses:
        default:
          description: "successful operation"
  /stats/facebookads/adgroups/customeventtype:
    get:
      tags:
      - "Stats Service"
      operationId: "getAdGroupCustomEventType"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              type: "string"
  /tiktok/webhook:
    post:
      tags:
      - "TikTok WH Service"
      operationId: "event"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "string"
  /user/settings:
    get:
      tags:
      - "User Settings Service"
      operationId: "getUserSettings"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/UserSettings"
  /user/unlock:
    post:
      tags:
      - "User Settings Service"
      operationId: "unlockUser"
      parameters: []
      responses:
        default:
          description: "successful operation"
  /mktp/session:
    post:
      tags:
      - "Vendasta Rest Service"
      operationId: "session"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/SessionToken"
  /mktp/purchase:
    get:
      tags:
      - "Vendasta Rest Service"
      operationId: "purchaseGET"
      consumes:
      - "*/*"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          type: "string"
      responses:
        default:
          description: "successful operation"
    post:
      tags:
      - "Vendasta Rest Service"
      operationId: "purchasePOST"
      consumes:
      - "*/*"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          type: "string"
      responses:
        default:
          description: "successful operation"
  /webhooks/{provider}/catch-all:
    get:
      tags:
      - "Webhook Base Api Service"
      operationId: "verifyWebhookSubscription"
      parameters:
      - name: "provider"
        in: "path"
        required: true
        type: "string"
      responses:
        default:
          description: "successful operation"
    post:
      tags:
      - "Webhook Base Api Service"
      operationId: "catchAllEvents"
      parameters:
      - name: "provider"
        in: "path"
        required: true
        type: "string"
      responses:
        default:
          description: "successful operation"
  /datastudio/datasets:
    get:
      tags:
      - "Looker studio connector Api Service"
      summary: "Return requested looker studio field values"
      description: ""
      operationId: "getTable"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/DatasetRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              type: "array"
              items:
                type: "object"
    post:
      tags:
      - "Looker studio connector Api Service"
      summary: "Return requested looker studio field values"
      description: ""
      operationId: "getTableWithPOST"
      consumes:
      - "application/x-www-form-urlencoded"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/DatasetRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              type: "array"
              items:
                type: "object"
  /datastudio/fbads/ads:
    get:
      tags:
      - "Data Studio Service"
      operationId: "getFacebookAds"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              $ref: "#/definitions/DataStudioAd"
  /datastudio/tiktokads/ads:
    get:
      tags:
      - "Data Studio Service"
      operationId: "getTikTokAds"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              $ref: "#/definitions/DataStudioAd"
  /v2/analytics/timelines:
    get:
      tags:
      - "Analytics Api Service"
      summary: "Returns a time series for a concrete metric during a period of time"
      description: ""
      operationId: "timeline"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "query"
        description: "network Supported values: <ul>\r\n<li>tiktok</li>\r\n<li>pinterest</li>\r\
          \n<li>youtube</li>\r\n<li>facebook</li>\r\n<li>gmb</li>\r\n<li>instagram</li>\r\
          \n<li>linkedin</li>\r\n</ul>"
        required: true
        type: "string"
      - name: "metric"
        in: "query"
        description: "metric Supported values: Metrics are case insensitive<ul>\r\n\
          <li>For TikTok Videos: videos, views, comments, shares, interactions, likes,\
          \ reach, engagement, impressionSources, averageVideoViews</li>\r\n<li>For\
          \ TikTok Account: video_views, profile_views, followers_count, followers_delta_count,\
          \ likes, comments, shares</li>\r\n<li>For Pinterest: impression save pin_click\
          \ outbound_click video_mrc_view video_avg_watch_time video_v50_watch_time\
          \ quartile_95_percent_view pins</li>\r\n<li>For Pinterest (accounts): followers,\
          \ following, delta followers</li>\r\n<li>For Youtube: views, interactions,\
          \ likes, dislikes, comments, shares </li>\r\n<li>For Facebook (metrics for\
          \ stories): storiesCount\r\n<li>For Facebook (metrics for posts): count,\
          \ interactions, engagement, impressionsunique, impressions, clicks, comments,\
          \ shares, reactions\r\n<li>For Facebook (metrics for reels): blue_reels_play_count,\
          \ post_impressions_unique, post_video_likes_by_reaction_type, post_video_social_actions,\
          \ engagement, count </li>\r\n<li>For Facebook (account metrics): page_posts_impressions,\
          \ page_actions_post_reactions_total, postsCount, postsInteractions, likes,\
          \ pageFollows, pageImpressions, pageImpressions.M, pageImpressions.F, pageImpressions.U,\
          \ pageImpressions.13-17, pageImpressions.18-24, pageImpressions.25-34, pageImpressions.35-44,\
          \ pageImpressions.45-54, pageImpressions.55-64, pageImpressions.65+, pageViews,\
          \ page_daily_follows_unique, page_daily_unfollows_unique</li>\r\n<li>For\
          \ GMB: business_impressions_maps, business_impressions_search, business_impressions_total,\
          \ business_direction_requests, call_clicks, website_clicks, clicks_total,\
          \ business_conversations, business_bookings, business_food_orders, business_actions_total</li>\r\
          \n<li>For Instagram (account metrics): email_contacts, get_directions_clicks,\
          \ phone_call_clicks, text_message_clicks, clicks_total, postsCount, postsInteractions</li>\r\
          \n<li>For Instagram (posts metrics): count, interactions, engagement, reach,\
          \ impressions, likes, comments, saves, shares</li>\r\n<li>For Instagram\
          \ (reels metrics): count, comments, likes, saved, shares, engagement, impressions,\
          \ reach, interactions, videoviews</li>\r\n<li>For Linkedin (account metrics\
          \ [company]): followers, paidFollowers, companyImpressions, deltaFollowers,\
          \ impressionCount, shareCount, clickCount, likeCount, commentCount, postsCount</li>\r\
          \n<li>For Linkedin (posts metrics [company]): posts, clicks, likes, comments,\
          \ shares, engagement, impressions, interactions</li>\r\n<li>For Linkedin\
          \ (newsletters metrics [company]): posts, clicks, likes, comments, shares,\
          \ engagement, impressions, interactions</li>\r\n<li>For Linkedin (account\
          \ metrics [personal]): followers, deltaFollowers, reaction, comment, reshare,\
          \ impression</li>\r\n<li>For Linkedin (posts metrics [personal]): count,\
          \ comment, reshare, impression, reaction, engagement, interactions</li>\r\
          \n<li>For Threads (posts metrics): count, views, likes, replies, reposts,\
          \ engagement, quotes, interactions</li>\r\n<li>For Bluesky (posts metrics):\
          \ posts_count, interactions, likes, replies, reposts, quotes</li>\r\n</ul>"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00+01:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "From Date and time in ISO 8601 format. e.g. 2021-09-10T03:30:00+01:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      - name: "subject"
        in: "query"
        description: "Is a filter when we retrieve data. Some examples: 'posts', 'reels',\
          \ 'account'. Each network defines its own 'subjects'"
        required: false
        type: "string"
      - name: "scope"
        in: "query"
        description: "Is a second filter. Some examples: 'viewed', 'published'. Now\
          \ its only used for Youtube"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseTimelineSeries"
  /v2/analytics/hashtags:
    get:
      tags:
      - "Analytics Api Service"
      operationId: "getPopularHashtags"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "query"
        required: false
        type: "string"
      - name: "q"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseHashtag"
  /v2/analytics/aggregation:
    get:
      tags:
      - "Analytics Api Service"
      operationId: "aggregation"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "query"
        required: true
        type: "string"
      - name: "metric"
        in: "query"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "subject"
        in: "query"
        required: false
        type: "string"
      - name: "scope"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseDouble"
  /v2/analytics/brand-summary/posts:
    get:
      tags:
      - "Analytics Api Service"
      operationId: "getBrandSummaryPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: false
        type: "string"
      - name: "to"
        in: "query"
        required: false
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseBrandSummaryPost"
  /v2/analytics/campaigns/tiktokads:
    get:
      tags:
      - "Analytics Api Service"
      operationId: "getTiktokAdsCampaigns"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "metrics[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseCampaign"
  /v2/analytics/distribution:
    get:
      tags:
      - "Analytics Api Service"
      operationId: "distribution"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "query"
        required: true
        type: "string"
      - name: "metric"
        in: "query"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "subject"
        in: "query"
        required: false
        type: "string"
      - name: "scope"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseDistributionItem"
  /v2/analytics/catalogs/{network}/scopes:
    get:
      tags:
      - "Analytics Catalogs ApiService"
      operationId: "verifyScopes"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseCollectionString"
  /v2/analytics/catalogs/accounts/youtube:
    get:
      tags:
      - "Analytics Catalogs ApiService"
      operationId: "getYoutubeAccountsByHandle"
      produces:
      - "application/json"
      parameters:
      - name: "handle"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseYoutubeCompetitor"
  /v2/analytics/catalogs/accounts/bluesky:
    get:
      tags:
      - "Analytics Catalogs ApiService"
      operationId: "getBlueskyAccountsByHandle"
      produces:
      - "application/json"
      parameters:
      - name: "handle"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseBlueskyCompetitor"
  /v2/analytics/posts/bluesky:
    get:
      tags:
      - "Bluesky Analytics Api Service"
      summary: "Returns the list of bluesky posts published during a period of time."
      description: ""
      operationId: "getPosts_1"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseBlueskyPost"
  /v2/analytics/bluesky/events/{type}:
    get:
      tags:
      - "Bluesky Analytics Api Service"
      summary: "Returns the list of bluesky accounts that follows and unfollows the\
        \ main account."
      description: ""
      operationId: "getBlueskyEvents"
      produces:
      - "application/json"
      parameters:
      - name: "type"
        in: "path"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "page"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - name: "pagesize"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/BlueskyEvent"
  /v2/analytics/competitors/{competitorId}/timelines:
    get:
      tags:
      - "Competitors Api Service"
      summary: "Returns a time series for a concrete metric during a period of time"
      description: ""
      operationId: "timeline_1"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "query"
        required: true
        type: "string"
      - name: "metric"
        in: "query"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "subject"
        in: "query"
        required: false
        type: "string"
      - name: "scope"
        in: "query"
        required: false
        type: "string"
      - name: "competitorId"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseTimelineSeries"
  /v2/analytics/competitors/{network}:
    get:
      tags:
      - "Competitors Api Service"
      operationId: "getCompetitors"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "path"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "string"
      - name: "competitors[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseInfluencer"
    post:
      tags:
      - "Competitors Api Service"
      operationId: "addCompetitor"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "path"
        required: true
        type: "string"
      - name: "id"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
    delete:
      tags:
      - "Competitors Api Service"
      operationId: "removeCompetitor"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "path"
        required: true
        type: "string"
      - name: "competitorId"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/analytics/competitors/{network}/{competitorId}:
    patch:
      tags:
      - "Competitors Api Service"
      operationId: "setFavorite"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "network"
        in: "path"
        required: true
        type: "string"
      - name: "competitorId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "fields"
        in: "query"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/Influencer"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseInfluencer"
  /v2/analytics/competitors/instagram/{competitorId}/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      summary: "Get posts of a IG competitor of a brand"
      description: ""
      operationId: "getInstagramCompetitorPosts"
      produces:
      - "application/json"
      parameters:
      - name: "competitorId"
        in: "path"
        description: "Competitor identifier"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        description: "From Date"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "From To"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "timezone"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        description: "number of posts to return (max of 5000 tweets)."
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseInstagramCompetitorMedia"
        404:
          description: "not found"
  /v2/analytics/competitors/instagram/{competitorId}/reels:
    get:
      tags:
      - "Competitors Posts Api Service"
      summary: "Get reels of a IG competitor of a brand"
      description: ""
      operationId: "getInstagramCompetitorReels"
      produces:
      - "application/json"
      parameters:
      - name: "competitorId"
        in: "path"
        description: "Competitor identifier"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        description: "From Date"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "From To"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "timezone"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        description: "number of posts to return (max of 5000 tweets)."
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseInstagramCompetitorMedia"
        404:
          description: "not found"
  /v2/analytics/competitors/twitter/{competitorId}/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      summary: "Get tweets of all competitors of a brand"
      description: ""
      operationId: "getTwitterCompetitorPosts"
      produces:
      - "application/json"
      parameters:
      - name: "competitorId"
        in: "path"
        description: "Competitor identifier"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        description: "From Date"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "timezone"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        description: "number of posts to return (max of 5000 tweets)."
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseCompetitorTweet"
        404:
          description: "not found"
  /v2/analytics/competitors/facebook/{competitorId}/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      summary: "Get posts of a FB competitor of a brand"
      description: ""
      operationId: "getFacebookCompetitorPosts"
      produces:
      - "application/json"
      parameters:
      - name: "competitorId"
        in: "path"
        description: "Competitor identifier"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        description: "From Date"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "From To"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "timezone"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        description: "number of posts to return (max of 5000 tweets)."
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseFacebookCompetitorPost"
        404:
          description: "not found"
  /v2/analytics/competitors/twitter/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      summary: "Get tweets of all competitors of a brand"
      description: ""
      operationId: "getBrandTwitterCompetitorsPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "timezone"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        description: "number of posts to return (max of 5000 tweets)."
        required: false
        type: "string"
      - name: "competitors[]"
        in: "query"
        description: "(Optional) Competitor id list to filter"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseCompetitorTweet"
        404:
          description: "not found"
  /v2/analytics/competitors/facebook/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      summary: "Get posts of all FB competitors of a brand"
      description: ""
      operationId: "getBrandFacebookCompetitorsPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "From To"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "timezone"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        description: "number of posts to return (max of 5000 tweets)."
        required: false
        type: "string"
      - name: "competitors[]"
        in: "query"
        description: "(Optional) Competitor id list to filter"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseFacebookCompetitorPost"
        404:
          description: "not found"
  /v2/analytics/competitors/instagram/publications:
    get:
      tags:
      - "Competitors Posts Api Service"
      summary: "Get publications (POSTS+REELS) of all IG competitors of a brand"
      description: ""
      operationId: "getBrandInstagramCompetitorsPublications"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "From To"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "timezone"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        description: "number of posts to return (max of 5000 tweets)."
        required: false
        type: "string"
      - name: "competitors[]"
        in: "query"
        description: "(Optional) Competitor id list to filter"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseInstagramCompetitorMedia"
        404:
          description: "not found"
  /v2/analytics/competitors/twitch/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      operationId: "getBrandTwitchCompetitorsPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "string"
      - name: "competitors[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseCompetitorTwitchVideo"
  /v2/analytics/competitors/twitch/{competitorId}/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      operationId: "getTwitchCompetitorPosts"
      produces:
      - "application/json"
      parameters:
      - name: "competitorId"
        in: "path"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseCompetitorTwitchVideo"
  /v2/analytics/competitors/twitch/{competitorId}/clips:
    get:
      tags:
      - "Competitors Posts Api Service"
      operationId: "getTwitchCompetitorClips"
      produces:
      - "application/json"
      parameters:
      - name: "competitorId"
        in: "path"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseCompetitorTwitchClip"
  /v2/analytics/competitors/youtube/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      operationId: "getBrandYoutubeCompetitorsPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "string"
      - name: "competitors[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseYouTubeCompetitorVideo"
  /v2/analytics/competitors/youtube/{competitorId}/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      operationId: "getYoutubeCompetitorPosts"
      produces:
      - "application/json"
      parameters:
      - name: "competitorId"
        in: "path"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseYouTubeCompetitorVideo"
  /v2/analytics/competitors/bluesky/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      operationId: "getBlueskyCompetitorsPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "string"
      - name: "competitors[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseBlueskyCompetitorPost"
  /v2/analytics/competitors/bluesky/{competitorId}/posts:
    get:
      tags:
      - "Competitors Posts Api Service"
      operationId: "getBlueskyCompetitorPostsByCompetitorId"
      produces:
      - "application/json"
      parameters:
      - name: "competitorId"
        in: "path"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "limit"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseBlueskyCompetitorPost"
  /v2/analytics/posts/facebook:
    get:
      tags:
      - "Facebook Analytics Service"
      summary: "Returns the list of Facebook posts created during a period of time."
      description: ""
      operationId: "getFacebookPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseFacebookPost"
  /v2/analytics/reels/facebook:
    get:
      tags:
      - "Facebook Analytics Service"
      summary: "Returns the list of Facebook reels created during a period of time."
      description: ""
      operationId: "getFacebookReels"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseFacebookReel"
  /v2/analytics/stories/facebook:
    get:
      tags:
      - "Facebook Analytics Service"
      summary: "Returns the list of Facebook stories created during a period of time."
      description: ""
      operationId: "getFacebookStories"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseFacebookStory"
  /v2/analytics/keywords/gbp:
    get:
      tags:
      - "Gbp Analytics Service"
      operationId: "getGbpKeywords"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseGbpKeyword"
  /v2/hashtags-tracker/tracking-sessions:
    get:
      tags:
      - "Hashtags Tracker Api Service"
      operationId: "getHashtagSessions"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseHashtagsTrackerSession"
    post:
      tags:
      - "Hashtags Tracker Api Service"
      operationId: "createSession"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/TrackSessionRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseHashtagsTrackerSession"
  /v2/hashtags-tracker/days:
    put:
      tags:
      - "Hashtags Tracker Api Service"
      operationId: "purchaseDays"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/PurchaseDaysRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponsePurchaseDaysResponse"
  /v2/hashtags-tracker/tracking-sessions/{id}/distribution:
    get:
      tags:
      - "Hashtags Tracker Api Service"
      operationId: "distributionHashtagsTracker"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      - name: "network"
        in: "query"
        required: true
        type: "string"
      - name: "metric"
        in: "query"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "subject"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseDistributionItem"
  /v2/hashtags-tracker/tracking-sessions/{id}/consolidations:
    post:
      tags:
      - "Hashtags Tracker Api Service"
      operationId: "executeManualSync"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      responses:
        default:
          description: "successful operation"
  /v2/analytics/posts/instagram/hashtags:
    get:
      tags:
      - "Instagram Analytics Service"
      summary: "Returns the list of Instagram hashtags used on posts created during\
        \ a period of time."
      description: ""
      operationId: "getInstagramPostsHashtags"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseInstagramHashtag"
  /v2/analytics/reels/instagram:
    get:
      tags:
      - "Instagram Analytics Service"
      summary: "Returns the list of Instagram reels created during a period of time."
      description: ""
      operationId: "getInstagramReels"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseInstagramReel"
  /v2/analytics/posts/instagram:
    get:
      tags:
      - "Instagram Analytics Service"
      summary: "Returns the list of Instagram posts created during a period of time."
      description: ""
      operationId: "getInstagramPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseInstagramPost"
  /v2/analytics/stories/instagram:
    get:
      tags:
      - "Instagram Analytics Service"
      summary: "Returns the list of Instagram stories created during a period of time."
      description: ""
      operationId: "getInstagramStories"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseInstagramStory"
  /v2/analytics/posts/linkedin:
    get:
      tags:
      - "Linkedin Analytics Service"
      summary: "Returns the list of Linkedin posts created during a period of time."
      description: ""
      operationId: "getPosts_2"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseLinkedinPost"
  /v2/analytics/newsletters/linkedin:
    get:
      tags:
      - "Linkedin Analytics Service"
      summary: "Returns the list of Linkedin newsletters created during a period of\
        \ time."
      description: ""
      operationId: "getNewsLetters"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseLinkedinPost"
  /v2/media/images:
    get:
      tags:
      - "Media Api Service"
      operationId: "searchPhotos"
      produces:
      - "application/json"
      parameters:
      - name: "query"
        in: "query"
        required: false
        type: "string"
      - name: "orientation"
        in: "query"
        required: false
        type: "string"
      - name: "size"
        in: "query"
        required: false
        type: "string"
      - name: "color"
        in: "query"
        required: false
        type: "string"
      - name: "lang"
        in: "query"
        required: false
        type: "string"
      - name: "page"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/PhotosSearchResponse"
  /v2/media/videos:
    get:
      tags:
      - "Media Api Service"
      operationId: "searchVideos"
      produces:
      - "application/json"
      parameters:
      - name: "query"
        in: "query"
        required: false
        type: "string"
      - name: "orientation"
        in: "query"
        required: false
        type: "string"
      - name: "size"
        in: "query"
        required: false
        type: "string"
      - name: "lang"
        in: "query"
        required: false
        type: "string"
      - name: "page"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - name: "minWidth"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - name: "minHeight"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - name: "minDuration"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - name: "maxDuration"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/VideosSearchResponse"
  /v2/media:
    put:
      tags:
      - "Media Api Service"
      operationId: "mergeUploadedChunks"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/MergeMediaRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseUploadMediaResponse"
  /v2/analytics/posts/pinterest:
    get:
      tags:
      - "Pinterest Analytics Api Service"
      operationId: "getPins"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponsePin"
  /v2/smart-links/links/{id}:
    get:
      tags:
      - "Smart Links Api Service"
      operationId: "getInfo"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseSmartLink"
    put:
      tags:
      - "Smart Links Api Service"
      operationId: "updateInfo"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/SmartLink"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseSmartLink"
    delete:
      tags:
      - "Smart Links Api Service"
      operationId: "delete"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/smart-links/links/{id}/analytics/buttons:
    get:
      tags:
      - "Smart Links Api Service"
      operationId: "getButtons"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseButtonRow"
  /v2/smart-links/links/slugs:
    get:
      tags:
      - "Smart Links Api Service"
      operationId: "isSlugAvailable"
      produces:
      - "application/json"
      parameters:
      - name: "value"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/smart-links/links:
    get:
      tags:
      - "Smart Links Api Service"
      operationId: "find"
      produces:
      - "application/json"
      parameters:
      - name: "slug"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseSmartLink"
    post:
      tags:
      - "Smart Links Api Service"
      operationId: "createSM"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/SmartLink"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseSmartLink"
  /v2/smart-links/links/{id}/analytics/timeline:
    get:
      tags:
      - "Smart Links Api Service"
      operationId: "timelineSM"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      - name: "metric"
        in: "query"
        required: true
        type: "string"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "itemId"
        in: "query"
        required: false
        type: "integer"
        format: "int64"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseTimelineSeries"
  /v2/smart-links/links/{id}/analytics/images:
    get:
      tags:
      - "Smart Links Api Service"
      operationId: "getImages"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseImageRow"
  /v2/analytics/posts/threads:
    get:
      tags:
      - "Threads Analytics Api Service"
      summary: "Returns the list of threads posts published during a period of time."
      description: ""
      operationId: "getPosts_3"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseThreadsPost"
  /v2/analytics/posts/tiktok:
    get:
      tags:
      - "TikTok Analytics Service"
      summary: "Returns the list of TikTok posts created during a period of time."
      description: ""
      operationId: "getTiktokPosts"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        description: "From Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        description: "To Date and time ISO 8601 format. e.g. 2021-01-01T10:00:00"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        description: "(Optional) The timezone used for the date range to search. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseTikTokPost"
  /v2/advertising/adgroups:
    get:
      tags:
      - "Adgroups Api Service"
      operationId: "getAdgroups"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "providers[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - name: "campaignId"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseAdgroup"
  /v2/advertising/ads:
    get:
      tags:
      - "Ads Api Service"
      operationId: "getAds"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "providers[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - name: "adgroupId"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseAd"
  /v2/advertising/ads/previews:
    post:
      tags:
      - "Ads Previews Api Service"
      operationId: "generatePreviews"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      - name: "format"
        in: "query"
        required: true
        type: "string"
      - name: "adPosition"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseAdPreview"
  /v2/advertising/campaigns:
    get:
      tags:
      - "Campaigns Service"
      operationId: "getCampaigns"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "providers[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseCampaign"
  /v2/advertising/ads/facebookads-accounts/{facebookAdsId}:
    get:
      tags:
      - "Facebook Ads Account Api Service"
      operationId: "getFbAdsAccountData"
      produces:
      - "application/json"
      parameters:
      - name: "facebookAdsId"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseFbAdsAccountData"
  /v2/advertising/keywords:
    get:
      tags:
      - "Keywords Api Service"
      operationId: "getKeywords"
      produces:
      - "application/json"
      parameters:
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "timezone"
        in: "query"
        required: false
        type: "string"
      - name: "campaignId"
        in: "query"
        required: false
        type: "string"
      - name: "adgroupId"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseKeyword"
  /v2/advertising/recommendations:
    get:
      tags:
      - "Recommendations Api Service"
      operationId: "getRecommendations"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseRecommendationsResponse"
    put:
      tags:
      - "Recommendations Api Service"
      operationId: "applyRecommendations"
      produces:
      - "application/json"
      parameters:
      - name: "ids[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseApplyRecommendationResult"
  /v2/advertising/recommendations/{recommendationId}:
    put:
      tags:
      - "Recommendations Api Service"
      operationId: "applyRecommendation"
      produces:
      - "application/json"
      parameters:
      - name: "recommendationId"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/advertising/suggestions/age:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getAge"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/advertising/suggestions/audiences-and-interests:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getAudiencesAndInterests"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      - name: "searchTerm"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseSuggestedItem"
  /v2/advertising/suggestions/locations:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getSuggestionsLocations"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      - name: "searchTerm"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseSuggestedLocation"
  /v2/advertising/suggestions/languages:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getLanguages"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseLanguagesSuggestionResponse"
  /v2/advertising/suggestions/audience-forecast:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getAudienceForecast"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseAudienceForecast"
  /v2/advertising/suggestions/pixels:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getPixels"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponsePixel"
  /v2/advertising/suggestions/conversion-events:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getConversionEvents"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseAdsCustomEvent"
  /v2/advertising/suggestions/currencies:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getCurrencies"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponsePlatformCurrency"
  /v2/advertising/suggestions/keywords:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getSuggestionsKeywords"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      - name: "searchTerm"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseSuggestedItem"
  /v2/advertising/suggestions/gender:
    post:
      tags:
      - "Suggestions Service"
      operationId: "getGender"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CampaignCreationState"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/agency-CK/{agencyId}/test-mail:
    post:
      tags:
      - "Agency Customization Kit Api Service"
      summary: "Send a test mail with the mail configuration."
      description: ""
      operationId: "sendTestMail"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        description: "Configuration needed to send Agency test mail."
        required: false
        schema:
          $ref: "#/definitions/AgencyTestMailData"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/agency-CK/details:
    get:
      tags:
      - "Agency Customization Kit Api Service"
      summary: "Get an Agency customization Kit"
      description: ""
      operationId: "getAgencyDetails"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseAgencyDetailsDto"
  /v2/agency-CK/{agencyId}:
    get:
      tags:
      - "Agency Customization Kit Api Service"
      summary: "Get an Agency customization Kit"
      description: ""
      operationId: "get"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseAgencyDto"
  /v2/agency-CK/{agencyId}/properties:
    patch:
      tags:
      - "Agency Customization Kit Api Service"
      summary: "Edit Agency configuration properties"
      description: ""
      operationId: "update"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - name: "fields"
        in: "query"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - in: "body"
        name: "body"
        description: "Configuration needed to set Agency properties."
        required: false
        schema:
          $ref: "#/definitions/AgencyPropertiesForUpdateDto"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseAgencyPropertiesForUpdateDto"
  /v2/agency-CK/{agencyId}/end-clients/{endClientId}/assignments:
    put:
      tags:
      - "Agency end-clients Api Service"
      summary: "Create or modify an end-client's brand assignment"
      description: ""
      operationId: "updateBrandAssignments"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - name: "endClientId"
        in: "path"
        description: "id of the end-client"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          type: "array"
          items:
            $ref: "#/definitions/AgencyEndClientBrandDto"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseAgencyEndClientBrandDto"
  /v2/agency-CK/{agencyId}/end-clients/{endClientId}/activation-link:
    post:
      tags:
      - "Agency end-clients Api Service"
      summary: "Resend Agency end-client invitation link"
      description: ""
      operationId: "resendActivationLink"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - name: "endClientId"
        in: "path"
        description: "id of the end-client"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/AgencyEndClientActivationLinkRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/agency-CK/{agencyId}/end-clients:
    get:
      tags:
      - "Agency end-clients Api Service"
      summary: "Get Agency end-clients"
      description: ""
      operationId: "get_1"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - name: "filter"
        in: "query"
        description: "(Optional) Json filter that must have a username \r\nIf the\
          \ filter is set, it returns the end-client with this username if exists,\
          \ \r\n if not, it returns an empty list"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseAgencyEndClientDto"
    post:
      tags:
      - "Agency end-clients Api Service"
      summary: "Add a new end-client to an Agency Customization Kit."
      description: ""
      operationId: "create"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        description: "Configuration needed to create an end-client."
        required: false
        schema:
          $ref: "#/definitions/AgencyEndClientCreationRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseAgencyEndClientDto"
  /v2/agency-CK/{agencyId}/end-clients/{endClientId}:
    delete:
      tags:
      - "Agency end-clients Api Service"
      summary: "Delete an end-client from an Agency Customization Kit."
      description: ""
      operationId: "delete_1"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - name: "endClientId"
        in: "path"
        description: "id of the end-client"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/agency-CK/{agencyId}/team-members/roles:
    get:
      tags:
      - "Agency team members Api Service"
      summary: "Get all available roles for Agency team members."
      description: ""
      operationId: "getRoles"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseTeamMemberRoleDto"
  /v2/agency-CK/{agencyId}/team-members:
    get:
      tags:
      - "Agency team members Api Service"
      summary: "Get all enabled Agency team members."
      description: ""
      operationId: "getTeamMembers"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseTeamMemberDto"
    post:
      tags:
      - "Agency team members Api Service"
      summary: "Add a new team member to an Agency."
      description: ""
      operationId: "create_1"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        description: "Configuration needed to create a team member."
        required: false
        schema:
          $ref: "#/definitions/AgencyTeamMembersCreationRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/agency-CK/{agencyId}/team-members/{teamMemberUserId}/invitation-email:
    post:
      tags:
      - "Agency team members Api Service"
      summary: "Resend Agency team member invitation email"
      description: ""
      operationId: "resendInvitationEmail"
      produces:
      - "application/json"
      parameters:
      - name: "agencyId"
        in: "path"
        description: "id of an Agency Customization Kit"
        required: true
        type: "integer"
        format: "int32"
      - name: "teamMemberUserId"
        in: "path"
        description: "userId of the team member"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/authorization/authorities:
    get:
      tags:
      - "Authorization Api Service"
      summary: "Get authorities of authenticated user"
      description: ""
      operationId: "getAuthoritiesFromToken"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseString"
  /v2/authorization/{userId}/collaborators/{collaboratorId}/activation-link:
    post:
      tags:
      - "Brand Role Collaborators Api Service"
      operationId: "resendActivationLink_1"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "collaboratorId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/EmailActivationInfo"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/authorization/{userId}/collaborators:
    get:
      tags:
      - "Brand Role Collaborators Api Service"
      operationId: "getBrandRoleCollaborators"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseBrandRoleCollaborator"
  /v2/authorization/{userId}/collaborators/{email}:
    post:
      tags:
      - "Brand Role Collaborators Api Service"
      operationId: "insertBrandRoleCollaborator"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "email"
        in: "path"
        required: true
        type: "string"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/BrandRoleAssignmentsRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBrandRoleCollaborator"
  /v2/authorization/{userId}/collaborators/{collaboratorId}:
    put:
      tags:
      - "Brand Role Collaborators Api Service"
      operationId: "updateBrandRoleAssignmentsByCollaboratorId"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "collaboratorId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          type: "array"
          items:
            $ref: "#/definitions/BrandRoleAssignment"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseBrandRoleAssignment"
    delete:
      tags:
      - "Brand Role Collaborators Api Service"
      operationId: "deleteBrandRoleCollaborator"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "collaboratorId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/authorization/{userId}/assignment:
    delete:
      tags:
      - "Brand Role Collaborators Api Service"
      operationId: "deleteBrandRoleAssignment"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "brandId"
        in: "query"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/authorization/{userId}/roles:
    get:
      tags:
      - "Brand Roles Api Service"
      operationId: "getRoles_1"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseBrandRole"
    post:
      tags:
      - "Brand Roles Api Service"
      operationId: "createBrandRole"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CreateBrandRoleRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBrandRole"
  /v2/authorization/{userId}/roles/{roleId}:
    delete:
      tags:
      - "Brand Roles Api Service"
      operationId: "deleteRole"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "roleId"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
    patch:
      tags:
      - "Brand Roles Api Service"
      operationId: "updateRole"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "roleId"
        in: "path"
        required: true
        type: "integer"
        format: "int64"
      - name: "fields"
        in: "query"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/UpdateBrandRoleRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBrandRole"
  /v2/chat:
    post:
      tags:
      - "Chat Api Service"
      summary: "Process chat request"
      description: ""
      operationId: "chat"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/ChatRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/ChatResponse"
  /v2/chat/{sessionId}:
    put:
      tags:
      - "Chat Api Service"
      summary: "Continue existing chat session"
      description: ""
      operationId: "continueChat"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "sessionId"
        in: "path"
        required: true
        type: "string"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/ChatRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/ChatResponse"
  /v2/features/check/{name}:
    get:
      tags:
      - "Feature Toggle Service"
      summary: "Check if feature is enabled for current user"
      description: "Checks if a feature is enabled for the authenticated user."
      operationId: "checkFeature"
      produces:
      - "application/json"
      parameters:
      - name: "name"
        in: "path"
        description: "Feature name"
        required: true
        type: "string"
      responses:
        200:
          description: "Success"
        401:
          description: "Unauthorized"
  /v2/features:
    get:
      tags:
      - "Feature Toggle Service"
      summary: "Get all feature toggles"
      description: "Retrieves all feature toggles. Admin access required."
      operationId: "getAllFeatures"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "Success"
        401:
          description: "Unauthorized"
        403:
          description: "Forbidden - Admin access required"
    post:
      tags:
      - "Feature Toggle Service"
      summary: "Create new feature toggle"
      description: "Creates a new feature toggle. Admin access required."
      operationId: "createFeature"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CreateFeatureToggleRequest"
      responses:
        200:
          description: "Feature toggle created successfully"
        400:
          description: "Bad request - Invalid input"
        401:
          description: "Unauthorized"
        403:
          description: "Forbidden - Admin access required"
        409:
          description: "Conflict - Feature name already exists"
  /v2/features/{id}:
    get:
      tags:
      - "Feature Toggle Service"
      summary: "Get feature toggle by ID"
      description: "Retrieves a specific feature toggle by ID. Admin access required."
      operationId: "getFeatureById"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "Feature toggle ID"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "Success"
        401:
          description: "Unauthorized"
        403:
          description: "Forbidden - Admin access required"
        404:
          description: "Feature toggle not found"
    put:
      tags:
      - "Feature Toggle Service"
      summary: "Update feature toggle"
      description: "Updates an existing feature toggle. Admin access required."
      operationId: "updateFeature"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "Feature toggle ID"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/UpdateFeatureToggleRequest"
      responses:
        200:
          description: "Feature toggle updated successfully"
        400:
          description: "Bad request - Invalid input"
        401:
          description: "Unauthorized"
        403:
          description: "Forbidden - Admin access required"
        404:
          description: "Feature toggle not found"
    delete:
      tags:
      - "Feature Toggle Service"
      summary: "Delete feature toggle"
      description: "Deletes a feature toggle. Admin access required."
      operationId: "deleteFeature"
      parameters:
      - name: "id"
        in: "path"
        description: "Feature toggle ID"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
        204:
          description: "Feature toggle deleted successfully"
        401:
          description: "Unauthorized"
        403:
          description: "Forbidden - Admin access required"
        404:
          description: "Feature toggle not found"
  /v2/features/enabled:
    get:
      tags:
      - "Feature Toggle Service"
      summary: "Get all enabled features for the logged user"
      description: "Returns all features that are enabled for the current user."
      operationId: "getEnabledFeatures"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseFeatureToggleDto"
  /v2/inbox/conversations:
    get:
      tags:
      - "Conversations Api Service"
      operationId: "getConversations"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseConversation"
    post:
      tags:
      - "Conversations Api Service"
      operationId: "postMessage"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/NewMessageRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/inbox/conversations/authorizations:
    get:
      tags:
      - "Conversations Api Service"
      summary: "Verify needed brand provider authorizations for Inbox feature by provider."
      description: ""
      operationId: "verifyAuthorizationsConversations"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "query"
        description: "Provider where you want to verify authorization. Example: INSTAGRAM,\
          \ TWITTER,..."
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseAuthorizations"
  /v2/inbox/conversations/fetch-image:
    get:
      tags:
      - "Conversations Api Service"
      operationId: "fetchImage"
      parameters:
      - name: "provider"
        in: "query"
        required: true
        type: "string"
      - name: "target"
        in: "query"
        required: false
        type: "string"
      responses:
        default:
          description: "successful operation"
  /v2/inbox/notes:
    get:
      tags:
      - "Inbox Notes Api Service"
      operationId: "getNotes"
      produces:
      - "application/json"
      parameters:
      - name: "participantScreenNames"
        in: "query"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - name: "participantAccountIds"
        in: "query"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - name: "provider"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseInboxNote"
    post:
      tags:
      - "Inbox Notes Api Service"
      operationId: "createNote"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/InboxNoteRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseInboxNote"
  /v2/inbox/notes/{noteId}:
    put:
      tags:
      - "Inbox Notes Api Service"
      operationId: "updateNote"
      produces:
      - "application/json"
      parameters:
      - name: "noteId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/InboxNoteRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseInboxNote"
    delete:
      tags:
      - "Inbox Notes Api Service"
      operationId: "deleteNote"
      produces:
      - "application/json"
      parameters:
      - name: "noteId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/inbox/status:
    put:
      tags:
      - "Inbox Status Change Api Service"
      operationId: "changeStatus"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/ChangeStatusRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/inbox/post-comments:
    get:
      tags:
      - "Post Comments Api Service"
      operationId: "getComments"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponsePostCommentsThread"
    post:
      tags:
      - "Post Comments Api Service"
      operationId: "postComment"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/NewCommentRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
    delete:
      tags:
      - "Post Comments Api Service"
      operationId: "deleteComment"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "query"
        required: true
        type: "string"
      - name: "commentId"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/inbox/post-comments/authorizations:
    get:
      tags:
      - "Post Comments Api Service"
      operationId: "verifyAuthorizationsComments"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseAuthorizations"
  /v2/inbox/reviews/replies:
    post:
      tags:
      - "Reviews Api Service"
      operationId: "postReply"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/NewReplyRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
    delete:
      tags:
      - "Reviews Api Service"
      operationId: "deleteReply"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/DeleteReplyRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/inbox/reviews:
    get:
      tags:
      - "Reviews Api Service"
      operationId: "getReviews"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseReview"
  /v2/integrations/ai/languages:
    get:
      tags:
      - "Ai Api Service"
      summary: "Get list of available AI languages"
      description: ""
      operationId: "getAvailableAILanguages"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseLanguageInfo"
  /v2/integrations/ai/{blogId}/system-prompts:
    get:
      tags:
      - "Ai Api Service"
      summary: "Get list of social media system prompts for a blog"
      description: ""
      operationId: "getSocialMediaSystemPrompts"
      produces:
      - "application/json"
      parameters:
      - name: "blogId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseSocialMediaSystemPromptResponse"
    delete:
      tags:
      - "Ai Api Service"
      summary: "Delete personalized system prompts for a blog"
      description: ""
      operationId: "customizeSystemPromptsForBlog_1"
      produces:
      - "application/json"
      parameters:
      - name: "blogId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "promptType"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseSystemPromptResponse"
    patch:
      tags:
      - "Ai Api Service"
      summary: "Customize system prompts for a blog"
      description: ""
      operationId: "customizeSystemPromptsForBlog"
      produces:
      - "application/json"
      parameters:
      - name: "blogId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/SocialMediaSystemPromptRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseSystemPromptResponse"
  /v2/integrations/ai/quick-actions/{quick-action}:
    post:
      tags:
      - "Ai Api Service"
      summary: "Process AI quick action"
      description: ""
      operationId: "getQuickActionResponse"
      produces:
      - "application/json"
      parameters:
      - name: "quick-action"
        in: "path"
        required: true
        type: "string"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/AssistantMessageRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseAssistantMessageResponse"
  /v2/integrations/ai/posts:
    post:
      tags:
      - "Ai Api Service"
      summary: "Create AI new post copy"
      description: ""
      operationId: "createAIPostCopy"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/AssistantMessageRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseAssistantMessageResponse"
  /v2/integrations/ai/posts{thread-id}:
    put:
      tags:
      - "Ai Api Service"
      summary: "Generate another AI post copy with or without context"
      description: ""
      operationId: "generateAnotherAIPostCopy"
      produces:
      - "application/json"
      parameters:
      - name: "thread-id"
        in: "path"
        required: true
        type: "string"
        pattern: "(/thread_(\\w+))?"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/VariantMessageRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseAssistantMessageResponse"
  /v2/integrations/ai/natural-language-scheduling:
    post:
      tags:
      - "Ai Natural Language Scheduling Api Service"
      summary: "Start natural language post processing job"
      description: ""
      operationId: "processNaturalLanguageJob"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/JobInfoRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseJobInfoResponse"
  /v2/integrations/ai/natural-language-scheduling/{jobId}:
    get:
      tags:
      - "Ai Natural Language Scheduling Api Service"
      summary: "Get job status and result for natural language post processing"
      description: ""
      operationId: "getNaturalLanguageJobInfo"
      produces:
      - "application/json"
      parameters:
      - name: "jobId"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseJobInfoResponse"
    patch:
      tags:
      - "Ai Natural Language Scheduling Api Service"
      summary: "Update the status of a natural language post processing job to cancelled"
      description: ""
      operationId: "cancelledJobStatus"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "jobId"
        in: "path"
        required: true
        type: "string"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/UpdateJobStatusRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseJobInfoResponse"
  /v2/integrations/ai/natural-language-scheduling/jobs:
    get:
      tags:
      - "Ai Natural Language Scheduling Api Service"
      summary: "Get list of job info for natural language post processing in last\
        \ 30 days"
      description: ""
      operationId: "getListOfNaturalLanguageJobs"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseJobInfoResponse"
  /v2/integrations/ai/natural-language-scheduling/{jobId}/posts:
    get:
      tags:
      - "Ai Natural Language Scheduling Api Service"
      summary: "Get list of posts scheduled by a natural language job"
      description: ""
      operationId: "getListOfNaturalLanguagePosts"
      produces:
      - "application/json"
      parameters:
      - name: "jobId"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseNaturalLanguageScheduledPostsResultDto"
  /v2/integrations/canva/disconnect:
    post:
      tags:
      - "Canva integration service"
      operationId: "disconnect"
      produces:
      - "application/json"
      parameters: []
      responses:
        default:
          description: "successful operation"
  /v2/integrations/canva/folders/{folderId}/items:
    get:
      tags:
      - "Canva integration service"
      operationId: "folder"
      produces:
      - "application/json"
      parameters:
      - name: "folderId"
        in: "path"
        required: true
        type: "string"
      - name: "continuation"
        in: "query"
        required: false
        type: "string"
      - name: "item_types"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - name: "sort_by"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/CanvaFolderContent"
  /v2/integrations/canva/designs:
    get:
      tags:
      - "Canva integration service"
      operationId: "designs"
      produces:
      - "application/json"
      parameters:
      - name: "query"
        in: "query"
        required: false
        type: "string"
      - name: "continuation"
        in: "query"
        required: false
        type: "string"
      - name: "ownership"
        in: "query"
        required: false
        type: "string"
      - name: "sort_by"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/CanvaUserDesigns"
  /v2/integrations/canva/exports:
    post:
      tags:
      - "Canva integration service"
      operationId: "startExportJob"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CanvaExportRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/CanvaExportJob"
  /v2/integrations/canva/exports/{exportId}:
    get:
      tags:
      - "Canva integration service"
      operationId: "canvaExportJobStatus"
      produces:
      - "application/json"
      parameters:
      - name: "exportId"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/CanvaExportJob"
  /v2/integrations/canva/me/profile:
    get:
      tags:
      - "Canva integration service"
      operationId: "profile"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/CanvaUserProfile"
  /v2/integrations/canva/me:
    get:
      tags:
      - "Canva integration service"
      operationId: "me"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/CanvaUserDetails"
  /v2/integrations/google-drive/disconnect:
    post:
      tags:
      - "Drive integration service"
      operationId: "disconnect_1"
      produces:
      - "application/json"
      parameters: []
      responses:
        default:
          description: "successful operation"
  /v2/integrations/google-drive/files/{fileId}:
    get:
      tags:
      - "Drive integration service"
      operationId: "getFileByFileId"
      produces:
      - "application/json"
      parameters:
      - name: "fileId"
        in: "path"
        required: true
        type: "string"
      - name: "alt"
        in: "query"
        required: false
        type: "string"
      - name: "supportsAllDrives"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/DriveFileResponse"
  /v2/integrations/google-drive/drives:
    post:
      tags:
      - "Drive integration service"
      operationId: "getDrivesList"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/DriveDrivesRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            type: "array"
            items:
              $ref: "#/definitions/DriveResponse"
  /v2/integrations/google-drive/files:
    post:
      tags:
      - "Drive integration service"
      operationId: "getUserFiles"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/DriveFilesRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/DriveFileListResponse"
  /v2/integrations/google-drive/me:
    get:
      tags:
      - "Drive integration service"
      operationId: "me_1"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/DriveUserDetailsResponse"
  /v2/partners/{partner}:
    get:
      tags:
      - "This endpoint returns the required configuration to embed Metricool in our\
        \ partners' sites"
      summary: "It returns the required configuration for a partner"
      description: ""
      operationId: "configuration"
      produces:
      - "application/json"
      parameters:
      - name: "partner"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/CustomizedUserConfiguration"
  /v2/analytics/reports/configuration:
    get:
      tags:
      - "Customize Report Api Service"
      operationId: "getReportConfigurations"
      produces:
      - "application/json"
      parameters:
      - name: "reportType"
        in: "query"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseReportConfiguration"
    put:
      tags:
      - "Customize Report Api Service"
      operationId: "updateReportConfigurations"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/ReportConfiguration"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseReportConfiguration"
  /v2/analytics/reports/demo:
    post:
      tags:
      - "Customize Report Api Service"
      summary: "Send demo report to user"
      description: ""
      operationId: "sendReportDemo"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "Mail to send with subject, text and receiver"
        required: false
        schema:
          $ref: "#/definitions/MailDemoReport"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/brands/{blogId}/reports/{jobId}:
    get:
      tags:
      - "Report Api Service"
      summary: "Get report status"
      description: ""
      operationId: "getReportStatusInfo"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/ReportRequest"
      - name: "blogId"
        in: "path"
        required: true
        type: "string"
      - name: "jobId"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseReportStatusInfo"
  /v2/brands/{blogId}/reports:
    get:
      tags:
      - "Report Api Service"
      summary: "Get list of report history items"
      description: ""
      operationId: "list"
      produces:
      - "application/json"
      parameters:
      - name: "blogId"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseReportHistoryItem"
  /v2/scheduler/tasks/{userId}:
    get:
      tags:
      - "Approval Task Api Service"
      operationId: "getApprovalTask"
      produces:
      - "application/json"
      parameters:
      - name: "editorStatus[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - name: "reviewerStatus[]"
        in: "query"
        required: false
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseApprovalTask"
  /v2/scheduler/tasks/{reviewerId}/count:
    get:
      tags:
      - "Approval Task Api Service"
      operationId: "getReviewerApprovalTaskCount"
      produces:
      - "application/json"
      parameters:
      - name: "reviewerId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "brandIdToReview"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseInteger"
  /v2/scheduler/tasks/{userId}/counters:
    get:
      tags:
      - "Approval Task Api Service"
      operationId: "getUserOpenedTasksCount"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseOpenedTasksCount"
  /v2/scheduler/besttimes/{provider}:
    get:
      tags:
      - "Best Times Api Service"
      summary: "Returns best time values to publish"
      description: ""
      operationId: "getBestTimes"
      produces:
      - "application/json"
      parameters:
      - name: "provider"
        in: "path"
        description: "supported values: facebook, instagram, tiktok, linkedin, youtube"
        required: true
        type: "string"
      - name: "start"
        in: "query"
        description: "The start date from you want to return the besttimes. ('2011-12-03T10:15:30')"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: "The date until you want to return the besttimes. ('2011-12-04T10:15:30')"
        required: false
        type: "string"
      - name: "timezone"
        in: "query"
        description: "The timezone in which you want to return the besttimes. ('Europe/Madrid')"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseBestTimes"
  /v2/scheduler/boards/pinterest:
    get:
      tags:
      - "Boards Api Service"
      operationId: "getPinterestBoards"
      produces:
      - "application/json"
      parameters:
      - name: "brandId"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseBoard"
    post:
      tags:
      - "Boards Api Service"
      operationId: "createPinterestBoard"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "brandId"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/Board"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoard"
  /v2/scheduler/catalogs/instagram/scopes:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "verifyScopes_1"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseCollectionString"
  /v2/scheduler/catalogs/instagram/eligibility:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "getInstagramShopProductTagEligibility"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/scheduler/catalogs/instagram:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "getInstagramCatalogs"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseIGCatalog"
  /v2/scheduler/catalogs/products/instagram:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "getInstagramCatalogProducts"
      produces:
      - "application/json"
      parameters:
      - name: "catalogId"
        in: "query"
        required: false
        type: "string"
      - name: "q"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseIGCatalogProduct"
  /v2/scheduler/catalogs/youtube/categories:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "getYoutubeCategories"
      produces:
      - "application/json"
      parameters:
      - name: "lang"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseListYoutubeVideoCategory"
  /v2/scheduler/catalogs/youtube/playlists:
    get:
      tags:
      - "Catalogs Api Service"
      summary: "Get YouTube playlists from YouTube"
      description: ""
      operationId: "getYoutubePlaylists"
      produces:
      - "application/json"
      parameters:
      - name: "refresh"
        in: "query"
        description: "If true, playlists will be refreshed from YouTube"
        required: false
        type: "boolean"
      responses:
        200:
          description: "Successful response"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/YoutubePlaylistDto"
        403:
          description: "Not authorized"
        500:
          description: "Internal server error"
  /v2/scheduler/catalogs/facebook/audio-recommendations:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "getFacebookAudioRecommendations"
      produces:
      - "application/json"
      parameters:
      - name: "type"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseFacebookRecommendedAudio"
  /v2/scheduler/catalogs/tiktok/scopes:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "verifyTiktokScopes"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseCollectionString"
  /v2/scheduler/catalogs/tiktok/creator-info:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "getTiktokCreatorInfo"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseTikTokCreatorInfo"
  /v2/scheduler/catalogs/tiktok/trending-tracks:
    get:
      tags:
      - "Catalogs Api Service"
      summary: "Get trending tracks from TikTok Business API"
      description: ""
      operationId: "getTiTokTrendingTracks"
      produces:
      - "application/json"
      parameters:
      - name: "genre"
        in: "query"
        description: "Optional - Filter by genre (default: ALL)"
        required: false
        type: "string"
      - name: "countryCode"
        in: "query"
        description: "Optional - Filter by country code (default: US)"
        required: false
        type: "string"
      - name: "dateRange"
        in: "query"
        description: "Optional - Filter by date range (default: 7DAY)"
        required: false
        type: "string"
      responses:
        200:
          description: "Successful response"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/TikTokTrendingTrackDto"
        403:
          description: "Not authorized (Business Account required)"
        500:
          description: "Internal server error"
  /v2/scheduler/catalogs/threads/geo-gating/eligibility:
    get:
      tags:
      - "Catalogs Api Service"
      operationId: "getThreadsGeoGatingEligibility"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/scheduler/counters:
    get:
      tags:
      - "Counters Api Service"
      operationId: "getCounters"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseSchedulerCounters"
  /v2/scheduler/calendars/{calendar-id}/cache:
    post:
      tags:
      - "ICS Calendar Rest Services for Metricool calendar (scheduler)"
      summary: "Refresh calendar cache and generate a new one by calendar ID for calendars\
        \ with type 'user'"
      description: ""
      operationId: "refreshCalendarCache"
      produces:
      - "application/json"
      parameters:
      - name: "calendar-id"
        in: "path"
        description: "Calendar ID"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "Cache refreshed and regenerated successfully"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        400:
          description: "Bad request"
        403:
          description: "Forbidden"
        500:
          description: "Internal server error"
  /v2/scheduler/calendars/metadata:
    get:
      tags:
      - "ICS Calendar Rest Services for Metricool calendar (scheduler)"
      summary: "Get calendar data from ics file url (don't store"
      description: ""
      operationId: "getCalendarFromURL"
      produces:
      - "application/json"
      parameters:
      - name: "url"
        in: "query"
        description: "Public url to ics calendar file"
        required: true
        type: "string"
      responses:
        200:
          description: "Ok"
          schema:
            $ref: "#/definitions/CalendarDto"
        404:
          description: "ics file don't found"
        400:
          description: "Bad request"
        403:
          description: "Forbidden"
  /v2/scheduler/calendars/{calendar-id}/assignation:
    post:
      tags:
      - "ICS Calendar Rest Services for Metricool calendar (scheduler)"
      summary: "Add calendar to user and/or blog, this calendar can be of two types:\
        \ system (internal calendars) and user (calendars updated by users)"
      description: ""
      operationId: "addCalendar"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "calendar-id"
        in: "path"
        description: "internal calendar id"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        description: "search-type user, blog or both(user & blog)"
        required: true
        schema:
          $ref: "#/definitions/Information about adding a calendar to an user or blog"
      responses:
        200:
          description: "Ok"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        204:
          description: "Not content"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        400:
          description: "Bad request"
        403:
          description: "Forbidden"
        500:
          description: "Internal server error"
    delete:
      tags:
      - "ICS Calendar Rest Services for Metricool calendar (scheduler)"
      summary: "Remove calendar (any calendar type) for user or blog"
      description: ""
      operationId: "removeCalendar"
      consumes:
      - "application/json"
      parameters:
      - name: "calendar-id"
        in: "path"
        description: "internal calendar id"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        description: "search-type user or brand"
        required: true
        schema:
          $ref: "#/definitions/Response about remove a calendar for an user or blog"
      responses:
        200:
          description: "Ok"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        400:
          description: "Bad request"
        403:
          description: "Forbidden"
        500:
          description: "Internal server error"
  /v2/scheduler/calendars:
    get:
      tags:
      - "ICS Calendar Rest Services for Metricool calendar (scheduler)"
      summary: "Get all system calendar data stored in database, only public"
      description: ""
      operationId: "findCalendars"
      produces:
      - "application/json"
      parameters:
      - name: "language"
        in: "query"
        description: "calendar language"
        required: false
        type: "string"
      responses:
        200:
          description: "Ok"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        204:
          description: "Not content"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        400:
          description: "Bad request"
        403:
          description: "Forbidden"
        500:
          description: "Internal server error"
  /v2/scheduler/calendars/assigned:
    get:
      tags:
      - "ICS Calendar Rest Services for Metricool calendar (scheduler)"
      summary: "Search all assigned calendars by mark or/and by user. Search all calendar\
        \ types system (internal calendars) and user (calendars updated by users)"
      description: ""
      operationId: "getSelectCalendars"
      produces:
      - "application/json"
      parameters:
      - name: "language"
        in: "query"
        description: "calendar language"
        required: false
        type: "string"
      responses:
        200:
          description: "Ok"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        204:
          description: "Not content"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        403:
          description: "Forbidden"
        500:
          description: "Internal server error"
  /v2/scheduler/calendars/{calendar-id}/events:
    get:
      tags:
      - "ICS Calendar Rest Services for Metricool calendar (scheduler)"
      summary: "get calendar with it events in time period"
      description: ""
      operationId: "getCalendarEvents"
      produces:
      - "application/json"
      parameters:
      - name: "initDate"
        in: "query"
        description: "init calendar period ('2025-02-01T00:00:00')"
        required: true
        type: "string"
      - name: "endDate"
        in: "query"
        description: "end calendar period ('2025-03-01T00:00:00')"
        required: true
        type: "string"
      - name: "timeZone"
        in: "query"
        description: "time zone"
        required: true
        type: "string"
      - name: "calendar-id"
        in: "path"
        description: "Calendar identification"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "Ok"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        204:
          description: "Not content"
          schema:
            $ref: "#/definitions/JsonOkResponse"
        400:
          description: "Bad request"
        403:
          description: "Forbidden"
        500:
          description: "Internal server error"
  /v2/scheduler/calendars/{calendar-type}:
    post:
      tags:
      - "ICS Calendar Rest Services for Metricool calendar (scheduler)"
      summary: "Create Calendar by type (ex: 'user', calendar with type user), and\
        \ assign it to the user or blog. Exclude internal types"
      description: ""
      operationId: "addTypeCalendar"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "public url to ics calendar file"
        required: true
        schema:
          $ref: "#/definitions/ICS calendar request data"
      - name: "calendar-type"
        in: "path"
        description: "Calendar type"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseICS Calendar Response Data"
        201:
          description: "Created"
          schema:
            $ref: "#/definitions/CalendarDto"
        400:
          description: "Bad request"
        403:
          description: "Forbidden"
        500:
          description: "Internal server error"
  /v2/scheduler/notifications-config:
    get:
      tags:
      - "Planner Notifications ApiService"
      operationId: "getConfiguration"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponsePlannerNotificationConfiguration"
    put:
      tags:
      - "Planner Notifications ApiService"
      operationId: "updateConfiguration"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/PlannerNotificationConfigurationRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponsePlannerNotificationConfiguration"
  /v2/scheduler/posts/{id}:
    get:
      tags:
      - "Posts Api Service"
      summary: "Get a scheduled post by id."
      description: ""
      operationId: "retrievePost"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the scheduled post."
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseScheduledPost"
    put:
      tags:
      - "Posts Api Service"
      summary: "Update an existing scheduled post."
      description: ""
      operationId: "update_1"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the post to update"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        description: "configuration needed to update a post"
        required: false
        schema:
          $ref: "#/definitions/ScheduledPost"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseScheduledPost"
    delete:
      tags:
      - "Posts Api Service"
      summary: "Delete the selected post by id. If the post belongs to a thread and\
        \ is the parent post, \r\nthis post and all those belonging to the thread,\
        \ will be deleted."
      description: ""
      operationId: "delete_2"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the scheduled post"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
    patch:
      tags:
      - "Posts Api Service"
      summary: "Edit and update a scheduled post. If the post belongs to a thread\
        \ and is the parent post, \r\nthis post and all those belonging to the thread,\
        \ will be updated."
      description: ""
      operationId: "updatePartial"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the post to update"
        required: true
        type: "integer"
        format: "int32"
      - name: "fields"
        in: "query"
        description: "list of fields to update"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - in: "body"
        name: "body"
        description: "configuration of the post to update"
        required: false
        schema:
          $ref: "#/definitions/ScheduledPostUpdateRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/scheduler/posts:
    get:
      tags:
      - "Posts Api Service"
      summary: "Get the scheduled posts between two dates or an uuid."
      description: ""
      operationId: "retrievePosts"
      produces:
      - "application/json"
      parameters:
      - name: "start"
        in: "query"
        description: "The start date from you want to return the posts. ('2011-12-03T10:15:30')"
        required: false
        type: "string"
      - name: "end"
        in: "query"
        description: "The date until you want to return the posts. ('2011-12-04T10:15:30')"
        required: false
        type: "string"
      - name: "timezone"
        in: "query"
        description: "The timezone in which you want to return the posts. ('Europe/Madrid')"
        required: false
        type: "string"
      - name: "filter"
        in: "query"
        description: "Json filter that must have publicationDate and providers or\
          \ a valid uuid\r\n(both are not allowed, just one uuid or just publicationDate\
          \ and providers)\r\nIf the filter is set none of the other params are taken\
          \ into account"
        required: false
        type: "string"
      - name: "extendedRange"
        in: "query"
        description: "(Optional) When it's true, search date range is expanded one\
          \ day after and one day before to\r\navoid timezone changes issues. Default\
          \ value is false"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseScheduledPost"
    post:
      tags:
      - "Posts Api Service"
      summary: "Creates a new scheduled post."
      description: ""
      operationId: "create_2"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "jobId"
        in: "query"
        description: "Optional job identifier"
        required: false
        type: "string"
      - in: "body"
        name: "body"
        description: "Configuration needed to schedule a post."
        required: false
        schema:
          $ref: "#/definitions/ScheduledPost"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseScheduledPost"
    put:
      tags:
      - "Posts Api Service"
      summary: "Send to review multiple posts of a brand in bulk."
      description: ""
      operationId: "updatePosts"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "Configuration needed to send to review multiple posts."
        required: false
        schema:
          $ref: "#/definitions/ScheduledPostApprovalDataInBulk"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseScheduledPostApprovalDataUpdateResponse"
  /v2/scheduler/posts/{id}/approvals:
    put:
      tags:
      - "Posts Api Service"
      summary: "Approve or reject a scheduled post by id and uuid."
      description: ""
      operationId: "updatePostApprovalEvent"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the scheduled post."
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        description: "JSON that represents the action of a reviewer."
        required: false
        schema:
          $ref: "#/definitions/ScheduledPostApprovalEventRequest"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/scheduler/posts/approvals-config:
    get:
      tags:
      - "Posts Api Service"
      summary: "Get the brand configuration needed to send a post to review."
      description: ""
      operationId: "getPostApprovalEvents"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBrandSchedulerPostApprovalData"
  /v2/scheduler/posts/instagram-properties:
    get:
      tags:
      - "Posts Api Service"
      summary: "Get Instagram auto-publish properties for authenticated brand."
      description: ""
      operationId: "getInstagramAutoPublishProperties"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseInstagramAutoPublishProperties"
  /v2/scheduler/posts/{uuid}/events:
    get:
      tags:
      - "Scheduled Post Events Api Service"
      operationId: "getPostEvents"
      produces:
      - "application/json"
      parameters:
      - name: "uuid"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseScheduledPostEventDto"
  /v2/scheduler/posts/{postId}/notes:
    get:
      tags:
      - "Scheduled Post Notes Api Service"
      operationId: "getScheduledPostNote"
      produces:
      - "application/json"
      parameters:
      - name: "postId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseScheduledPostNote"
    post:
      tags:
      - "Scheduled Post Notes Api Service"
      operationId: "createScheduledPostNote"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "postId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "sourcePostId"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/ScheduledPostNoteRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseScheduledPostNote"
  /v2/scheduler/posts/{postId}/notes/{noteId}:
    put:
      tags:
      - "Scheduled Post Notes Api Service"
      operationId: "updateScheduledPostNote"
      produces:
      - "application/json"
      parameters:
      - name: "postId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "noteId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/ScheduledPostNoteRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseScheduledPostNote"
    delete:
      tags:
      - "Scheduled Post Notes Api Service"
      operationId: "deleteScheduledPostNoteScheduler"
      produces:
      - "application/json"
      parameters:
      - name: "postId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "noteId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/scheduler/posts/{postId}/notes/status:
    put:
      tags:
      - "Scheduled Post Notes Api Service"
      operationId: "setScheduledPostNotesStatus"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "postId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/scheduler/library/posts/{id}/events:
    get:
      tags:
      - "Posts Api Service"
      summary: "Get a library post events by id."
      description: ""
      operationId: "retrieveEvents"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the library post."
        required: true
        type: "integer"
        format: "int64"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseLibraryPostEventDto"
  /v2/scheduler/library/posts:
    get:
      tags:
      - "Posts Api Service"
      summary: "Get all library posts of a brand."
      description: ""
      operationId: "retrievePosts_1"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseLibraryPostDto"
    post:
      tags:
      - "Posts Api Service"
      summary: "Creates a new library post."
      description: ""
      operationId: "create_3"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "Configuration needed to create a library post."
        required: false
        schema:
          $ref: "#/definitions/LibraryPostDto"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseLibraryPostDto"
  /v2/scheduler/library/posts/{id}:
    get:
      tags:
      - "Posts Api Service"
      summary: "Get a library post by id."
      description: ""
      operationId: "retrievePost_1"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the library post."
        required: true
        type: "integer"
        format: "int64"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseLibraryPostDto"
    put:
      tags:
      - "Posts Api Service"
      summary: "Update an existing library post."
      description: ""
      operationId: "update_2"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the post to update"
        required: true
        type: "integer"
        format: "int64"
      - in: "body"
        name: "body"
        description: "configuration needed to update a library post"
        required: false
        schema:
          $ref: "#/definitions/LibraryPostDto"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseLibraryPostDto"
    delete:
      tags:
      - "Posts Api Service"
      summary: "Delete the selected library post by id. If the post belongs to a thread\
        \ and is the parent post, \r\nthis post and all those belonging to the thread,\
        \ will be deleted."
      description: ""
      operationId: "delete_3"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        description: "id of the library post"
        required: true
        type: "integer"
        format: "int64"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/settings/brands/{brand-id}/images:
    get:
      tags:
      - "Brands Api Service"
      operationId: "fetchImage_1"
      parameters:
      - name: "brand-id"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "provider"
        in: "query"
        required: true
        type: "string"
      responses:
        default:
          description: "successful operation"
    delete:
      tags:
      - "Brands Api Service"
      operationId: "deleteBrandImage"
      produces:
      - "application/json"
      parameters:
      - name: "brand-id"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/settings/brands/ip-filters:
    get:
      tags:
      - "Brands Api Service"
      operationId: "getIpFilters"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseIpFiltersResponse"
    post:
      tags:
      - "Brands Api Service"
      operationId: "postIpFilters"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseIpFiltersResponse"
    delete:
      tags:
      - "Brands Api Service"
      operationId: "deleteIpFilters"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseIpFiltersResponse"
  /v2/settings/brands/{brand-id}:
    get:
      tags:
      - "Brands Api Service"
      operationId: "getBrand"
      produces:
      - "application/json"
      parameters:
      - name: "brand-id"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBrand"
    patch:
      tags:
      - "Brands Api Service"
      operationId: "updateBrand"
      produces:
      - "application/json"
      parameters:
      - name: "brand-id"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "fields"
        in: "query"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/Brand"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBrand"
  /v2/settings/brands:
    get:
      tags:
      - "Brands Api Service"
      summary: "Returns a list of brands for the current user."
      description: ""
      operationId: "getBrands"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseBrandLite"
  /v2/settings/brands/engagement-ratio:
    put:
      tags:
      - "Brands Api Service"
      operationId: "saveEngagementRatioInAllMyManagedBrands"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/EngagementRatioValue"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
