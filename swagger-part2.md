  /v2/settings/brands/{brand-id}/feed:
    get:
      tags:
      - "Brands Api Service"
      operationId: "getBrandFeed"
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
            $ref: "#/definitions/JsonOkResponseBrandFeed"
    put:
      tags:
      - "Brands Api Service"
      operationId: "setBrandFeed"
      produces:
      - "application/json"
      parameters:
      - name: "brand-id"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/BrandFeed"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBrandFeed"
  /v2/settings/brands/connections/{provider}:
    delete:
      tags:
      - "Connections V2 Api Service"
      operationId: "disconnect_2"
      parameters:
      - name: "provider"
        in: "path"
        required: true
        type: "string"
      responses:
        default:
          description: "successful operation"
  /v2/settings/brands/connections/instagram/media-feed:
    get:
      tags:
      - "Connections V2 Api Service"
      operationId: "getInstagramMedia"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseInstagramFeedMedia"
  /v2/settings/brands/connections/tiktok:
    post:
      tags:
      - "Connections V2 Api Service"
      operationId: "createTiktokConnection"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/BrandProfile"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseString"
  /v2/settings/brands/connections/facebook:
    post:
      tags:
      - "Connections V2 Api Service"
      operationId: "createFacebookConnection"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/FacebookConnectionRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/settings/catalogs/countries:
    get:
      tags:
      - "Countries Api Service"
      operationId: "getCountries"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseCountry"
  /v2/settings/catalogs/countries/{region}/regions:
    get:
      tags:
      - "Countries Api Service"
      operationId: "getStates"
      produces:
      - "application/json"
      parameters:
      - name: "region"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseState"
  /v2/settings/payment-methods/{paymentMethodToken}:
    delete:
      tags:
      - "Payment Methods Api Service"
      operationId: "deletePaymentMethod"
      produces:
      - "application/json"
      parameters:
      - name: "paymentMethodToken"
        in: "path"
        required: true
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/settings/payment-methods:
    get:
      tags:
      - "Payment Methods Api Service"
      operationId: "getUserPaymentMethods"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseUserPaymentMethods"
  /v2/settings/subscriptions/current:
    get:
      tags:
      - "Subscriptions Api Service"
      operationId: "getCurrentSubscription"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseSubscription"
  /v2/settings/subscription-plans:
    get:
      tags:
      - "Subscriptions Api Service"
      operationId: "getSubscriptionPlans"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseSubscriptionPlan"
  /v2/settings/subscriptions:
    post:
      tags:
      - "Subscriptions Api Service"
      operationId: "createSubscription"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/CreateSubscriptionRequest"
      responses:
        default:
          description: "successful operation"
    put:
      tags:
      - "Subscriptions Api Service"
      operationId: "updateSubscription"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/SubscriptionChangeRequest"
      responses:
        default:
          description: "successful operation"
    delete:
      tags:
      - "Subscriptions Api Service"
      operationId: "cancelSubscription"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/SubscriptionCancelRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/settings/subscription/coupon/{couponCode}:
    get:
      tags:
      - "Subscriptions Api Service"
      operationId: "applyCoupon"
      produces:
      - "application/json"
      parameters:
      - name: "couponCode"
        in: "path"
        required: true
        type: "string"
      - name: "planId"
        in: "query"
        required: false
        type: "string"
      - name: "addons.twitter"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - name: "previousBalance"
        in: "query"
        required: false
        type: "number"
        format: "double"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseCouponResult"
  /v2/settings/subscriptions/prorated-discount:
    get:
      tags:
      - "Subscriptions Api Service"
      operationId: "getProratedDiscount"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseFloat"
  /v2/settings/third-party-apps:
    get:
      tags:
      - "Third Party Apps Api Service"
      summary: "Returns the list of connected apps"
      description: ""
      operationId: "connectedApplications"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/Application"
  /v2/settings/third-party-apps/{clientId}:
    delete:
      tags:
      - "Third Party Apps Api Service"
      summary: "Revoke access to a client"
      description: ""
      operationId: "revokeConnection"
      produces:
      - "application/json"
      parameters:
      - name: "clientId"
        in: "path"
        required: true
        type: "string"
      responses:
        default:
          description: "successful operation"
  /v2/settings/catalogs/timezones:
    get:
      tags:
      - "Timezones Api Service"
      operationId: "getTimezones"
      produces:
      - "application/json"
      parameters: []
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseTimezone"
  /v2/settings/users/{id}:
    get:
      tags:
      - "Users Api Service"
      operationId: "getUser"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseUser"
    delete:
      tags:
      - "Users Api Service"
      operationId: "deleteAccount"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "id"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/DeleteUserRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
    patch:
      tags:
      - "Users Api Service"
      operationId: "updateUserSettings"
      produces:
      - "application/json"
      parameters:
      - name: "id"
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
          $ref: "#/definitions/UpdateUserRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseUser"
  /v2/settings/users/{id}/credentials:
    patch:
      tags:
      - "Users Api Service"
      operationId: "updateUserCredentials"
      produces:
      - "application/json"
      parameters:
      - name: "id"
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
          $ref: "#/definitions/UpdateUserCredentialsRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseUserCredentials"
  /v2/settings/users/saved-texts:
    get:
      tags:
      - "Users Api Service"
      operationId: "getSavedTexts"
      produces:
      - "application/json"
      parameters:
      - name: "savedTextType"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseSavedTextWithPermissions"
    post:
      tags:
      - "Users Api Service"
      operationId: "createSavedText"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - name: "savedTextType"
        in: "query"
        required: false
        type: "string"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/SavedTextRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseSavedText"
  /v2/settings/users/saved-texts/{savedTextId}:
    put:
      tags:
      - "Users Api Service"
      operationId: "updateSavedText"
      produces:
      - "application/json"
      parameters:
      - name: "savedTextType"
        in: "query"
        required: false
        type: "string"
      - name: "savedTextId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/SavedTextRequest"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseSavedText"
    delete:
      tags:
      - "Users Api Service"
      operationId: "deleteScheduledPostNote"
      produces:
      - "application/json"
      parameters:
      - name: "savedTextType"
        in: "query"
        required: false
        type: "string"
      - name: "savedTextId"
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
  /v2/settings/users/saved-texts/tags:
    get:
      tags:
      - "Users Api Service"
      operationId: "getTagsFromSavedTexts"
      produces:
      - "application/json"
      parameters:
      - name: "savedTextType"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseStTagCount"
  /v2/settings/users:
    get:
      tags:
      - "Users Api Service"
      operationId: "getUserInfo"
      produces:
      - "application/json"
      parameters:
      - name: "authorization"
        in: "header"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseUser"
    head:
      tags:
      - "Users Api Service"
      operationId: "existsUserWithEmail"
      produces:
      - "application/json"
      parameters:
      - name: "email"
        in: "query"
        required: true
        type: "string"
      responses:
        default:
          description: "successful operation"
    patch:
      tags:
      - "Users Api Service"
      operationId: "updateRecoveryCredentials"
      produces:
      - "application/json"
      parameters:
      - name: "authorization"
        in: "header"
        required: false
        type: "string"
      - in: "body"
        name: "body"
        required: false
        schema:
          $ref: "#/definitions/RecoveryChangeRequest"
      - name: "fields"
        in: "query"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseBoolean"
  /v2/settings/users/{userId}/api-usage-stats:
    get:
      tags:
      - "Users Api Service"
      operationId: "getUserStatisticsForPeriod"
      produces:
      - "application/json"
      parameters:
      - name: "userId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "from"
        in: "query"
        required: true
        type: "string"
      - name: "to"
        in: "query"
        required: true
        type: "string"
      - name: "aggregation"
        in: "query"
        required: false
        type: "string"
      - name: "includeEndpoints"
        in: "query"
        required: false
        type: "boolean"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkListResponseApiConsumptionData"
  /v2/settings/users/{userId}/linkedin-trial/eligibility:
    get:
      tags:
      - "Users Api Service"
      summary: "Get eligibility for linkedin trial"
      description: ""
      operationId: "checkTrialEligibility"
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
          schema:
            $ref: "#/definitions/JsonOkResponseTrialEligibilityResponse"
  /v2/settings/users/{userId}/linkedin-trial/info:
    get:
      tags:
      - "Users Api Service"
      summary: "Get information for linkedin trial"
      description: ""
      operationId: "getTrialInformation"
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
          schema:
            $ref: "#/definitions/JsonOkResponseTrialInfoResponse"
  /v2/settings/whitelabel/logininfo/{blogId}:
    get:
      tags:
      - "Whitelabel Settings Api Service"
      operationId: "getToken"
      produces:
      - "application/json"
      parameters:
      - name: "scope"
        in: "query"
        required: false
        type: "string"
      - name: "expm"
        in: "query"
        required: false
        type: "integer"
        format: "int32"
      - name: "networks"
        in: "query"
        required: false
        type: "string"
      - name: "role"
        in: "query"
        required: false
        type: "string"
      - name: "blogId"
        in: "path"
        required: true
        type: "integer"
        format: "int32"
      - name: "redirect"
        in: "query"
        required: false
        type: "string"
      - name: "dlprop"
        in: "query"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          headers: {}
          schema:
            $ref: "#/definitions/JsonOkResponseLoginInfo"
  /v2/settings/users/{userid}/legal-terms:
    get:
      tags:
      - "Legal terms api"
      summary: "Search user legal terms by status"
      description: ""
      operationId: "getLegalTerms"
      parameters:
      - name: "userid"
        in: "path"
        description: "User to search"
        required: true
        type: "integer"
        format: "int32"
      - name: "status"
        in: "query"
        description: "Status to filter (only Pending at this momment)"
        required: false
        type: "string"
      responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/JsonOkListResponseLegalTermDto"
  /v2/settings/users/{userid}/contract-events:
    post:
      tags:
      - "User contract events api service"
      summary: "Register legal conditions change acceptation"
      description: ""
      operationId: "registerContractEvent"
      parameters:
      - name: "userid"
        in: "path"
        description: "User who accepts"
        required: true
        type: "integer"
        format: "int32"
      - in: "body"
        name: "body"
        description: "Accepted change"
        required: false
        schema:
          $ref: "#/definitions/ContractEventRequest"
      responses:
        default:
          description: "successful operation"
definitions:
  BrandRole:
    type: "object"
    required:
    - "actions"
    - "userId"
    properties:
      id:
        type: "integer"
        format: "int64"
      userId:
        type: "integer"
        format: "int32"
      name:
        type: "string"
      description:
        type: "string"
      color:
        type: "string"
      type:
        type: "string"
      assignable:
        type: "boolean"
      deletedDate:
        $ref: "#/definitions/DateTimeInfo"
      deleted:
        type: "boolean"
      actions:
        $ref: "#/definitions/BrandRoleActions"
      assignedUsersCount:
        type: "integer"
        format: "int32"
      assignedEnabledCount:
        type: "integer"
        format: "int32"
      assignedDisabledCount:
        type: "integer"
        format: "int32"
  BrandRoleActions:
    type: "object"
    properties:
      viewAnalytics:
        type: "boolean"
      viewInbox:
        type: "boolean"
      viewPlanner:
        type: "boolean"
      viewAds:
        type: "boolean"
      viewSmartlinks:
        type: "boolean"
      fullAccessReports:
        type: "boolean"
      fullAccessInbox:
        type: "boolean"
      fullAccessPlanner:
        type: "boolean"
      fullAccessAds:
        type: "boolean"
      fullAccessSmartlinks:
        type: "boolean"
      fullAccessHashtagTracker:
        type: "boolean"
      editBrand:
        type: "boolean"
      schedulePosts:
        type: "boolean"
      publishPosts:
        type: "boolean"
      approvePosts:
        type: "boolean"
      viewCondensedAnalytics:
        type: "boolean"
  DateTimeInfo:
    type: "object"
    required:
    - "dateTime"
    properties:
      dateTime:
        type: "string"
      timezone:
        type: "string"
  PublicBlog:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      ownerUserId:
        type: "integer"
        format: "int32"
      label:
        type: "string"
      url:
        type: "string"
      title:
        type: "string"
      description:
        type: "string"
      picture:
        type: "string"
      twitter:
        type: "string"
      facebook:
        type: "string"
      facebookPageId:
        type: "string"
      facebookGroup:
        type: "string"
      facebookGroupId:
        type: "string"
      instagram:
        type: "string"
      fbBusinessId:
        type: "string"
      googlePlus:
        type: "string"
      linkedinCompany:
        type: "string"
      facebookAds:
        type: "string"
      adwords:
        type: "string"
      gmb:
        type: "string"
      youtube:
        type: "string"
      twitch:
        type: "string"
      tiktokads:
        type: "string"
      pinterest:
        type: "string"
      tiktok:
        type: "string"
      threads:
        type: "string"
      bluesky:
        type: "string"
      feedRss:
        type: "string"
      tiktokAccountType:
        type: "string"
        enum:
        - "BUSINESS"
        - "PERSONAL"
      instagramConnectionType:
        type: "string"
        enum:
        - "BUSINESS"
        - "FACEBOOK_LOGIN"
      twitterPicture:
        type: "string"
      twitterSubscriptionType:
        type: "string"
      facebookPicture:
        type: "string"
      facebookGroupPicture:
        type: "string"
      instagramPicture:
        type: "string"
      linkedInPicture:
        type: "string"
      facebookAdsPicture:
        type: "string"
      facebookAdsName:
        type: "string"
      pinterestPicture:
        type: "string"
      pinterestBusiness:
        type: "boolean"
      tiktokPicture:
        type: "string"
      tiktokBusinessTokenExpiration:
        type: "string"
      threadsPicture:
        type: "string"
      threadsAccountName:
        type: "string"
      blueskyPicture:
        type: "string"
      blueskyHandle:
        type: "string"
      fbUserId:
        type: "string"
      inUserId:
        type: "string"
      adwordsUserId:
        type: "string"
      adwordsAccountName:
        type: "string"
      gmbUserId:
        type: "string"
      gmbAccountName:
        type: "string"
      gmbAddress:
        type: "string"
      gmbUrl:
        type: "string"
      tiktokadsUserId:
        type: "string"
      linkedInCompanyPicture:
        type: "string"
      linkedInCompanyName:
        type: "string"
      linkedInTokenExpiration:
        type: "string"
      linkedInUserProfileURL:
        type: "string"
      youtubeChannelName:
        type: "string"
      youtubeChannelPicture:
        type: "string"
      twitchName:
        type: "string"
      twitchPicture:
        type: "string"
      twitchChannelId:
        type: "string"
      tiktokadsDisplayName:
        type: "string"
      tiktokadsPicture:
        type: "string"
      tiktokUserProfileUrl:
        type: "string"
      isShared:
        type: "boolean"
      ownerUsername:
        type: "string"
      whiteLabelLink:
        type: "string"
      analyticModeWhitelabelLink:
        type: "string"
      whiteLabelAlias:
        type: "string"
      hash:
        type: "string"
      version:
        type: "integer"
        format: "int64"
      frontendVersion:
        type: "string"
      role:
        type: "string"
      deleteDate:
        type: "string"
        format: "date-time"
      deleted:
        type: "boolean"
      joinDate:
        type: "string"
        format: "date-time"
      firstConnectionDate:
        type: "string"
        format: "date-time"
      lastResolvedInboxMessageTimestamp:
        type: "integer"
        format: "int64"
      lastReadInboxMessageTimestamp:
        type: "integer"
        format: "int64"
      timezone:
        type: "string"
      availableConnectors:
        type: "array"
        items:
          type: "string"
      brandRole:
        $ref: "#/definitions/BrandRole"
      isWhiteLabel:
        type: "boolean"
      isWhiteLabelOnlyRead:
        type: "boolean"
      engagementRatio:
        type: "integer"
        format: "int32"
      hasXOAuth2Token:
        type: "boolean"
      isDemo:
        type: "boolean"
  TemplateReport:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      name:
        type: "string"
      userId:
        type: "integer"
        format: "int64"
      deleted:
        type: "integer"
        format: "int32"
      blogId:
        type: "integer"
        format: "int32"
  ImageObject:
    type: "object"
    properties:
      type:
        type: "string"
      id:
        type: "string"
      title:
        type: "string"
      previewUrl:
        type: "string"
      originalUrl:
        type: "string"
  PageInfo:
    type: "object"
    properties:
      offset:
        type: "integer"
        format: "int32"
      count:
        type: "integer"
        format: "int32"
  SearchResponse:
    type: "object"
    properties:
      data:
        type: "array"
        items:
          $ref: "#/definitions/ImageObject"
      pageInfo:
        $ref: "#/definitions/PageInfo"
  InstagramLinkTree:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      blogId:
        type: "integer"
        format: "int32"
      link:
        type: "string"
      text:
        type: "string"
      position:
        type: "integer"
        format: "int32"
      color:
        type: "string"
      linkId:
        type: "integer"
        format: "int32"
      shortUrl:
        type: "string"
  InstagramBioCatalog:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      blogId:
        type: "integer"
        format: "int32"
      postId:
        type: "string"
      timestamp:
        type: "integer"
        format: "int64"
      url:
        type: "string"
      imageUrl:
        type: "string"
      linkId:
        type: "integer"
        format: "int32"
      shortUrl:
        type: "string"
      type:
        type: "string"
  FacebookLocation:
    type: "object"
    properties:
      name:
        type: "string"
      link:
        type: "string"
      id:
        type: "string"
      location:
        $ref: "#/definitions/FacebookLocationCoordinates"
  FacebookLocationCoordinates:
    type: "object"
    properties:
      city:
        type: "string"
      country:
        type: "string"
      latitude:
        type: "number"
        format: "double"
      longitude:
        type: "number"
        format: "double"
      state:
        type: "string"
      street:
        type: "string"
      zip:
        type: "string"
  TwitterEvent:
    type: "object"
    properties:
      twitterId:
        type: "integer"
        format: "int64"
      date:
        type: "integer"
        format: "int32"
      screenName:
        type: "string"
      fullName:
        type: "string"
      picture:
        type: "string"
      url:
        type: "string"
      description:
        type: "string"
      followers:
        type: "integer"
        format: "int32"
      friends:
        type: "integer"
        format: "int32"
      isFollowedByMe:
        type: "boolean"
      isFollowingMe:
        type: "boolean"
      isMuted:
        type: "boolean"
      isBlocked:
        type: "boolean"
      isProtected:
        type: "boolean"
      isVerified:
        type: "boolean"
      lastActivity:
        type: "integer"
        format: "int64"
      statusId:
        type: "string"
      tweetMedia:
        type: "string"
      strCreated:
        type: "string"
  CalendarCSVRow:
    type: "object"
    properties:
      text:
        type: "string"
      date:
        type: "string"
      time:
        type: "string"
      draft:
        type: "string"
      facebook:
        type: "string"
      twitter:
        type: "string"
      linkedIn:
        type: "string"
      gmb:
        type: "string"
      instagram:
        type: "string"
      imageUrl1:
        type: "string"
      imageUrl2:
        type: "string"
      imageUrl3:
        type: "string"
      imageUrl4:
        type: "string"
      imageUrl5:
        type: "string"
      imageUrl6:
        type: "string"
      imageUrl7:
        type: "string"
      imageUrl8:
        type: "string"
      imageUrl9:
        type: "string"
      imageUrl10:
        type: "string"
      shortener:
        type: "string"
  UserSettingsReportSections:
    type: "object"
    properties:
      reportMonthlyDownload:
        type: "string"
      reportMonthlyMail:
        type: "string"
      reportLogo:
        type: "string"
      reportMonthlyMailText:
        type: "string"
      reportMonthlyDate:
        type: "integer"
        format: "int32"
  InfluencersRestrictions:
    type: "object"
    properties:
      twitter:
        type: "integer"
        format: "int32"
      facebook:
        type: "integer"
        format: "int32"
      youtube:
        type: "integer"
        format: "int32"
      instagram:
        type: "integer"
        format: "int32"
      twitch:
        type: "integer"
        format: "int32"
  Subscription:
    type: "object"
    properties:
      id:
        type: "string"
      provider:
        type: "string"
      providerUrl:
        type: "string"
      userId:
        type: "integer"
        format: "int32"
      created:
        type: "string"
      planId:
        type: "string"
      status:
        type: "string"
      paymentMethodToken:
        type: "string"
      nextPaymentDateInDays:
        type: "integer"
        format: "int32"
      nextPaymentDate:
        $ref: "#/definitions/DateTimeInfo"
      nextPaymentAmount:
        type: "number"
        format: "float"
      taxData:
        $ref: "#/definitions/TaxData"
      usedProfiles:
        type: "integer"
        format: "int32"
      usedPosts:
        type: "integer"
        format: "int32"
      maxProfiles:
        type: "integer"
        format: "int32"
      maxPosts:
        type: "integer"
        format: "int32"
      maxPostsPerBrand:
        type: "integer"
        format: "int32"
      maxAICreditsPerBrand:
        type: "integer"
        format: "int32"
      plan:
        $ref: "#/definitions/SubscriptionPlan"
      immediatelyCancelable:
        type: "boolean"
      downgradeSubscription:
        $ref: "#/definitions/Subscription"
      addons:
        type: "object"
        additionalProperties:
          $ref: "#/definitions/AddonData"
      adhocPlan:
        type: "boolean"
      trialInProgress:
        type: "boolean"
  SubscriptionPlan:
    type: "object"
    properties:
      id:
        type: "string"
      name:
        type: "string"
      billingCycles:
        type: "integer"
        format: "int32"
      price:
        type: "number"
        format: "float"
      profiles:
        type: "integer"
        format: "int32"
      tweets:
        type: "integer"
        format: "int32"
      maxPostsPerBrand:
        type: "integer"
        format: "int32"
      shareProfiles:
        type: "boolean"
      whiteLabel:
        type: "boolean"
      influencers:
        type: "boolean"
      instagramBioLink:
        type: "boolean"
      reportTemplate:
        type: "boolean"
      currency:
        type: "string"
      reportDownload:
        type: "boolean"
      historyMaxDays:
        type: "integer"
        format: "int64"
      influencersRestrictions:
        $ref: "#/definitions/InfluencersRestrictions"
      stripePriceId:
        type: "string"
      level:
        type: "integer"
        format: "int32"
      annualDiscountPercent:
        type: "number"
        format: "float"
      maxAICopiesByBrandPerMonth:
        type: "integer"
        format: "int32"
      api:
        type: "boolean"
      dataLockerStudio:
        type: "boolean"
      zapier:
        type: "boolean"
      addons:
        type: "object"
        additionalProperties:
          $ref: "#/definitions/AddonData"
  DMUserMention:
    type: "object"
    properties:
      screenName:
        type: "string"
      name:
        type: "string"
      idStr:
        type: "string"
      id:
        type: "integer"
        format: "int64"
  DMVariant:
    type: "object"
    properties:
      contentType:
        type: "string"
      url:
        type: "string"
      bitRate:
        type: "integer"
        format: "int32"
  DMVideoInfo:
    type: "object"
    properties:
      variants:
        type: "array"
        items:
          $ref: "#/definitions/DMVariant"
  ExtendedTweet:
    type: "object"
    properties:
      fullText:
        type: "string"
      entities:
        $ref: "#/definitions/TwitterEntities"
  Tweet:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      id:
        type: "integer"
        format: "int64"
      idStr:
        type: "string"
      userId:
        type: "integer"
        format: "int64"
      createdAt:
        type: "string"
        format: "date-time"
      text:
        type: "string"
      updatedAt:
        type: "string"
        format: "date-time"
      favoriteCount:
        type: "integer"
        format: "int32"
      retweetCount:
        type: "integer"
        format: "int32"
      linkClicks:
        type: "integer"
        format: "int32"
      promoted:
        type: "boolean"
      metricsV2:
        type: "object"
        additionalProperties:
          type: "object"
      userName:
        type: "string"
      screenName:
        type: "string"
      followers:
        type: "integer"
        format: "int64"
      impressions:
        type: "integer"
        format: "int64"
      imageUrl:
        type: "string"
      timestamp:
        type: "integer"
        format: "int64"
      source:
        type: "string"
      interactions:
        type: "integer"
        format: "int64"
      engagement:
        type: "number"
        format: "double"
      picture:
        type: "string"
      ownerPicture:
        type: "string"
      hasVideo:
        type: "boolean"
      hasPhoto:
        type: "boolean"
      hasUrls:
        type: "boolean"
      isRetweet:
        type: "boolean"
      inReplyToScreenName:
        type: "string"
      inReplyToStatusIdStr:
        type: "string"
      inReplyToStatusId:
        type: "integer"
        format: "int64"
      user:
        $ref: "#/definitions/TwitterProfile"
      retweetedStatus:
        $ref: "#/definitions/Tweet"
      entities:
        $ref: "#/definitions/TwitterEntities"
      extendedEntities:
        $ref: "#/definitions/TwitterExtendedEntities"
      coordinates:
        $ref: "#/definitions/TwitterCoordinates"
      extendedTweet:
        $ref: "#/definitions/ExtendedTweet"
      truncated:
        type: "boolean"
      created:
        type: "string"
        format: "date-time"
      retweets:
        type: "integer"
        format: "int32"
      favorites:
        type: "integer"
        format: "int32"
      retweet:
        type: "boolean"
      tweetId:
        type: "string"
      hasMedia:
        type: "boolean"
      hasTags:
        type: "boolean"
      lang:
        type: "string"
  TwitterCoordinates:
    type: "object"
    properties:
      type:
        type: "string"
      coordinates:
        type: "array"
        items:
          type: "number"
          format: "float"
      latitude:
        type: "number"
        format: "float"
      longitude:
        type: "number"
        format: "float"
  TwitterEntities:
    type: "object"
    properties:
      hashtags:
        type: "array"
        items:
          $ref: "#/definitions/TwitterHashtag"
      userMentions:
        type: "array"
        items:
          $ref: "#/definitions/DMUserMention"
      media:
        type: "array"
        items:
          $ref: "#/definitions/TwitterMedia"
      urls:
        type: "array"
        items:
          $ref: "#/definitions/TwitterUrl"
  TwitterExtendedEntities:
    type: "object"
    properties:
      hashtags:
        type: "array"
        items:
          $ref: "#/definitions/TwitterHashtag"
      userMentions:
        type: "array"
        items:
          $ref: "#/definitions/DMUserMention"
  TwitterHashtag:
    type: "object"
    properties:
      text:
        type: "string"
  TwitterMedia:
    type: "object"
    properties:
      id:
        type: "string"
      type:
        type: "string"
      mediaUrl:
        type: "string"
      mediaUrlHttps:
        type: "string"
      videoInfo:
        $ref: "#/definitions/DMVideoInfo"
      mediaSecureUrl:
        type: "string"
  TwitterProfile:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      screenName:
        type: "string"
      profileImageUrl:
        type: "string"
      profileBannerUrl:
        type: "string"
      url:
        type: "string"
      description:
        type: "string"
      followersCount:
        type: "integer"
        format: "int32"
      listedCount:
        type: "integer"
        format: "int32"
      createdAt:
        type: "integer"
        format: "int64"
      email:
        type: "string"
      idStr:
        type: "string"
      timeZone:
        type: "string"
      language:
        type: "string"
      location:
        type: "string"
      verified:
        type: "boolean"
      status:
        $ref: "#/definitions/Tweet"
      followers:
        type: "integer"
        format: "int32"
      profileUrl:
        type: "string"
      name:
        type: "string"
      profile_image_url_https:
        type: "string"
      picture:
        type: "string"
        readOnly: true
      profile_background_image_url_https:
        type: "string"
      profile_background_color:
        type: "string"
      statuses_count:
        type: "integer"
        format: "int32"
      friends_count:
        type: "integer"
        format: "int32"
      favourites_count:
        type: "integer"
        format: "int32"
      protected:
        type: "boolean"
      subscription_type:
        type: "string"
  TwitterUrl:
    type: "object"
    properties:
      url:
        type: "string"
      expandedUrl:
        type: "string"
      displayUrl:
        type: "string"
  PublicPost:
    type: "object"
    properties:
      postUrl:
        type: "string"
      title:
        type: "string"
      excerpt:
        type: "string"
      date:
        type: "string"
        format: "date-time"
      commentsCount:
        type: "integer"
        format: "int32"
      picture:
        type: "string"
      twShares:
        type: "integer"
        format: "int32"
      fbShares:
        type: "integer"
        format: "int32"
      inShares:
        type: "integer"
        format: "int32"
      pinShares:
        type: "integer"
        format: "int32"
      totalShares:
        type: "integer"
        format: "int32"
      pageViews:
        type: "integer"
        format: "int64"
      totalPageViews:
        type: "integer"
        format: "int64"
  VisitorEvent:
    type: "object"
    properties:
      index:
        type: "integer"
        format: "int64"
      url:
        type: "string"
      fromUrl:
        type: "string"
      country:
        type: "string"
      region:
        type: "string"
      device:
        type: "string"
      browser:
        type: "string"
      date:
        type: "integer"
        format: "int64"
  VisitorSession:
    type: "object"
    properties:
      lastUrl:
        type: "string"
      fromUrl:
        type: "string"
      country:
        type: "string"
      region:
        type: "string"
      device:
        type: "string"
      browser:
        type: "string"
      firstDate:
        type: "integer"
        format: "int64"
      lastDate:
        type: "integer"
        format: "int64"
      pagesCount:
        type: "integer"
        format: "int32"
      events:
        type: "array"
        items:
          $ref: "#/definitions/VisitorEvent"
  VisitorSessionList:
    type: "object"
    properties:
      sessions:
        type: "array"
        items:
          $ref: "#/definitions/VisitorSession"
      timeline:
        type: "object"
        additionalProperties:
          type: "integer"
          format: "int64"
  InstagramPost:
    type: "object"
    properties:
      postId:
        type: "string"
      userId:
        type: "string"
      businessId:
        type: "string"
      type:
        type: "string"
      publishedAt:
        $ref: "#/definitions/DateTimeInfo"
      filter:
        type: "string"
      url:
        type: "string"
      content:
        type: "string"
      imageUrl:
        type: "string"
      likes:
        type: "integer"
        format: "int32"
      comments:
        type: "integer"
        format: "int32"
      shares:
        type: "integer"
        format: "int32"
      interactions:
        type: "integer"
        format: "int64"
      engagement:
        type: "number"
        format: "double"
      reach:
        type: "integer"
        format: "int32"
      saved:
        type: "integer"
        format: "int32"
      impressionsPaid:
        type: "integer"
        format: "int32"
      impressionsTotal:
        type: "integer"
        format: "int32"
      views:
        type: "integer"
        format: "int32"
      reachPaid:
        type: "integer"
        format: "int32"
      videoViewsPaid:
        type: "integer"
        format: "int32"
      videoViewsTotal:
        type: "integer"
        format: "int32"
      postClicksPaid:
        type: "integer"
        format: "int32"
      postInteractionsPaid:
        type: "integer"
        format: "int32"
      spend:
        type: "number"
        format: "double"
      hashtags:
        type: "array"
        items:
          type: "string"
      clicks:
        type: "number"
        format: "double"
      impressions:
        type: "integer"
        format: "int32"
  InstagramReel:
    type: "object"
    properties:
      reelId:
        type: "string"
      userId:
        type: "string"
      businessId:
        type: "string"
      type:
        type: "string"
      publishedAt:
        $ref: "#/definitions/DateTimeInfo"
      filter:
        type: "string"
      url:
        type: "string"
      content:
        type: "string"
      imageUrl:
        type: "string"
      likes:
        type: "integer"
        format: "int32"
      comments:
        type: "integer"
        format: "int32"
      interactions:
        type: "integer"
        format: "int64"
      engagement:
        type: "number"
        format: "double"
      views:
        type: "integer"
        format: "int32"
      reach:
        type: "integer"
        format: "int32"
      saved:
        type: "integer"
        format: "int32"
      shares:
        type: "integer"
        format: "int32"
      impressionsPaid:
        type: "integer"
        format: "int32"
      impressionsTotal:
        type: "integer"
        format: "int32"
      reachPaid:
        type: "integer"
        format: "int32"
      videoViewsPaid:
        type: "integer"
        format: "int32"
      videoViewsTotal:
        type: "integer"
        format: "int32"
      postClicksPaid:
        type: "integer"
        format: "int32"
      postInteractionsPaid:
        type: "integer"
        format: "int32"
      spend:
        type: "number"
        format: "double"
      videoViews:
        type: "integer"
        format: "int32"
      impressions:
        type: "integer"
        format: "int32"
  InstagramStory:
    type: "object"
    properties:
      postId:
        type: "string"
      businessId:
        type: "string"
      type:
        type: "string"
      publishedAt:
        $ref: "#/definitions/DateTimeInfo"
      owner:
        type: "string"
      content:
        type: "string"
      thumbnailUrl:
        type: "string"
      mediaUrl:
        type: "string"
      permalink:
        type: "string"
      exits:
        type: "integer"
        format: "int32"
      impressions:
        type: "integer"
        format: "int32"
      reach:
        type: "integer"
        format: "int32"
      replies:
        type: "integer"
        format: "int32"
      tapsForward:
        type: "integer"
        format: "int32"
      tapsBack:
        type: "integer"
        format: "int32"
      impressionsPaid:
        type: "integer"
        format: "int32"
      impressionsTotal:
        type: "integer"
        format: "int32"
      reachPaid:
        type: "integer"
        format: "int32"
  Number:
    type: "object"
  GenderAgeDistribution:
    type: "object"
    properties:
      gender:
        type: "string"
      age:
        type: "string"
      value:
        $ref: "#/definitions/Number"
  TwitchVideo:
    type: "object"
    properties:
      channelId:
        type: "string"
      videoId:
        type: "string"
      thumbnailUrl:
        type: "string"
      videoUrl:
        type: "string"
      title:
        type: "string"
      created:
        type: "string"
        format: "date-time"
      createdTimestamp:
        type: "string"
        format: "date-time"
      game:
        type: "string"
      duration:
        type: "number"
        format: "double"
      views:
        type: "number"
        format: "double"
      averageViews:
        type: "number"
        format: "double"
      clips:
        type: "integer"
        format: "int32"
      clipId:
        type: "string"
      clipUrl:
        type: "string"
      videoNameForClip:
        type: "string"
      videoUrlForClip:
        type: "string"
      ownerScreenName:
        type: "string"
      ownerDisplayName:
        type: "string"
      ownerPicture:
        type: "string"
  TwitchClip:
    type: "object"
    properties:
      channelId:
        type: "string"
      videoId:
        type: "string"
      thumbnailUrl:
        type: "string"
      clipId:
        type: "string"
      title:
        type: "string"
      created:
        type: "string"
        format: "date-time"
      createdTimestamp:
        type: "string"
        format: "date-time"
      game:
        type: "string"
      views:
        type: "number"
        format: "double"
      clipUrl:
        type: "string"
      videoNameForClip:
        type: "string"
      videoUrlForClip:
        type: "string"
  TwitchSubscription:
    type: "object"
    properties:
      broadcasterId:
        type: "string"
      subscriberId:
        type: "string"
      date:
        type: "string"
        format: "date-time"
      subscriberName:
        type: "string"
      type:
        type: "string"
      isGift:
        type: "boolean"
      picture:
        type: "string"
      profileUrl:
        type: "string"
      gifterName:
        type: "string"
      gifterId:
        type: "string"
  AdCampaign:
    type: "object"
    properties:
      adAccount:
        type: "string"
      customEventType:
        type: "string"
      objective:
        type: "string"
      provider:
        type: "string"
      providerCampaignId:
        type: "string"
      conversions:
        type: "number"
        format: "double"
      actions:
        type: "object"
        additionalProperties:
          type: "number"
          format: "double"
      id:
        type: "integer"
        format: "int64"
      providerId:
        type: "string"
      name:
        type: "string"
      buying_type:
        type: "string"
      status:
        type: "string"
      created:
        type: "string"
        format: "date-time"
      start:
        type: "string"
        format: "date-time"
      stop:
        type: "string"
        format: "date-time"
      updated:
        type: "string"
        format: "date-time"
      date:
        type: "integer"
        format: "int32"
      impressions:
        type: "number"
        format: "double"
      reach:
        type: "number"
        format: "double"
      clicks:
        type: "number"
        format: "double"
      spent:
        type: "number"
        format: "double"
      uniqueClicks:
        type: "number"
        format: "double"
      uniqueCtr:
        type: "number"
        format: "double"
      advertisingChannelType:
        type: "string"
      advertisingChannelSubType:
        type: "string"
      biddingStrategyType:
        type: "string"
      budgetId:
        type: "string"
      budget:
        type: "number"
        format: "double"
      budgetType:
        type: "string"
        enum:
        - "DAILY"
        - "LIFETIME"
      purchaseROAS:
        type: "number"
        format: "double"
      allConversionsValue:
        type: "number"
        format: "double"
      conversionsValue:
        type: "number"
        format: "double"
      costPerConversion:
        type: "number"
        format: "double"
      ctr:
        type: "number"
        format: "double"
      impressionsReach:
        type: "number"
        format: "double"
      averageCost:
        type: "number"
        format: "double"
      averageCpc:
        type: "number"
        format: "double"
      averageCpe:
        type: "number"
        format: "double"
      averageCpm:
        type: "number"
        format: "double"
      averageCpv:
        type: "number"
        format: "double"
      averageCpp:
        type: "number"
        format: "double"
      averagePageViews:
        type: "number"
        format: "double"
      averagePosition:
        type: "number"
        format: "double"
      historicalQualityScore:
        type: "number"
        format: "double"
      country:
        type: "string"
      currency:
        type: "string"
      conversionRate:
        type: "number"
        format: "double"
      results:
        type: "number"
        format: "double"
      resultsLabel:
        type: "string"
      gadsCtr:
        type: "number"
        format: "double"
      cpm:
        type: "number"
        format: "double"
      cpc:
        type: "number"
        format: "double"
  FacebookPost:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      pageId:
        type: "string"
      postId:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      timestamp:
        type: "integer"
        format: "int64"
      link:
        type: "string"
      text:
        type: "string"
      type:
        type: "string"
      shares:
        type: "integer"
        format: "int32"
      comments:
        type: "integer"
        format: "int32"
      reactions:
        type: "integer"
        format: "int32"
      impressions:
        type: "integer"
        format: "int32"
      impressionsPaid:
        type: "integer"
        format: "int32"
      impressionsOrganic:
        type: "integer"
        format: "int32"
      impressionsUnique:
        type: "integer"
        format: "int32"
      impressionsUniquePaid:
        type: "integer"
        format: "int32"
      impressionsUniqueOrganic:
        type: "integer"
        format: "int32"
      clicks:
        type: "integer"
        format: "int32"
      engagement:
        type: "number"
        format: "double"
      picture:
        type: "string"
      videoViews:
        type: "integer"
        format: "int32"
      videoViewsPaid:
        type: "integer"
        format: "int32"
      videoViewsOrganic:
        type: "integer"
        format: "int32"
      videoTimeWatched:
        type: "integer"
        format: "int32"
      linkclicks:
        type: "integer"
        format: "int32"
      spend:
        type: "number"
        format: "double"
      ownerScreenName:
        type: "string"
      ownerDisplayName:
        type: "string"
      ownerPicture:
        type: "string"
      internalSearchId:
        type: "string"
  LinkedinPost:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      companyId:
        type: "string"
      postId:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      clicks:
        type: "integer"
        format: "int32"
      comments:
        type: "integer"
        format: "int32"
      likes:
        type: "integer"
        format: "int32"
      shares:
        type: "integer"
        format: "int32"
      impressions:
        type: "integer"
        format: "int32"
      uniqueImpressions:
        type: "integer"
        format: "int32"
      engagement:
        type: "number"
        format: "double"
      videoViews:
        type: "integer"
        format: "int32"
      viewers:
        type: "integer"
        format: "int32"
      timeWatched:
        type: "integer"
        format: "int32"
      timeWatchedForVideoViews:
        type: "integer"
        format: "int32"
      url:
        type: "string"
      description:
        type: "string"
      title:
        type: "string"
      picture:
        type: "string"
      comment:
        type: "string"
      type:
        type: "string"
  AdsKeyword:
    type: "object"
    properties:
      provider:
        type: "string"
      date:
        type: "integer"
        format: "int32"
      adAccount:
        type: "string"
      name:
        type: "string"
      id:
        type: "string"
      matchType:
        type: "string"
      allConversions:
        type: "number"
        format: "double"
      allConversionsValue:
        type: "number"
        format: "double"
      averageCost:
        type: "number"
        format: "double"
      averageCPC:
        type: "number"
        format: "double"
      averageCPM:
        type: "number"
        format: "double"
      clicks:
        type: "integer"
        format: "int64"
      ctr:
        type: "number"
        format: "double"
      cost:
        type: "number"
        format: "double"
      engagements:
        type: "integer"
        format: "int32"
      impressions:
        type: "integer"
        format: "int32"
      interactions:
        type: "integer"
        format: "int32"
      conversions:
        type: "number"
        format: "double"
      conversionsValue:
        type: "number"
        format: "double"
      campId:
        type: "string"
      adGroupId:
        type: "string"
      campName:
        type: "string"
      adGroupName:
        type: "string"
      status:
        type: "string"
      costPerConversion:
        type: "number"
        format: "double"
      averageCPE:
        type: "number"
        format: "double"
      averageCPV:
        type: "number"
        format: "double"
      averagePageViews:
        type: "number"
        format: "double"
      averagePosition:
        type: "number"
        format: "double"
      historicalCreativeQualityScore:
        type: "number"
        format: "double"
      historicalLandingPageQualityScore:
        type: "number"
        format: "double"
      historicalQualityScore:
        type: "number"
        format: "double"
      historicalSearchPredictedCtr:
        type: "number"
        format: "double"
      maxCPC:
        type: "number"
        format: "double"
      biddingStrategy:
        type: "string"
      conversionRate:
        type: "number"
        format: "double"
      purchaseROAS:
        type: "number"
        format: "double"
  Ad:
    type: "object"
    properties:
      name:
        type: "string"
      businessName:
        type: "string"
      website:
        type: "string"
      titles:
        type: "array"
        items:
          type: "string"
      descriptions:
        type: "array"
        items:
          type: "string"
      logoUrl:
        type: "string"
      mediaItems:
        type: "array"
        items:
          $ref: "#/definitions/MediaItem"
  GmbReview:
    type: "object"
    properties:
      name:
        type: "string"
      text:
        type: "string"
      reviewerName:
        type: "string"
      reviewerPhoto:
        type: "string"
      created:
        type: "string"
        format: "date-time"
      updated:
        type: "string"
        format: "date-time"
      starRating:
        type: "integer"
        format: "int32"
      replied:
        type: "integer"
        format: "int32"
      replyComment:
        type: "string"
      locationId:
        type: "string"
  GmbMedia:
    type: "object"
    properties:
      ownerName:
        type: "string"
      ownerUrl:
        type: "string"
      ownerPhotoUrl:
        type: "string"
      created:
        type: "string"
        format: "date-time"
      photoUrl:
        type: "string"
      mediaFormat:
        type: "string"
      mediaId:
        type: "string"
      type:
        type: "string"
      text:
        type: "string"
      mediaUrl:
        type: "string"
      viewsCount:
        type: "integer"
        format: "int64"
  Blog:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      label:
        type: "string"
      labelImg:
        type: "string"
      labelImgDefault:
        type: "string"
      name:
        type: "string"
      type:
        type: "string"
      blogger:
        $ref: "#/definitions/User"
      created:
        type: "integer"
        format: "int64"
      management_key:
        type: "string"
      twitter:
        type: "string"
      facebook:
        type: "string"
      fbGroup:
        type: "string"
      facebookAds:
        type: "string"
      facebookBusinessId:
        type: "string"
      googlePlus:
        type: "string"
      title:
        type: "string"
      description:
        type: "string"
      hash:
        type: "string"
      joined:
        type: "string"
        format: "date-time"
      purpose:
        type: "string"
      instagram:
        type: "string"
      linkedInCompany:
        type: "string"
      adwords:
        type: "string"
      pinterest:
        type: "string"
      gmb:
        type: "string"
      twitch:
        type: "string"
      youtube:
        type: "string"
      tiktokads:
        type: "string"
      tiktok:
        type: "string"
      threads:
        type: "string"
      bluesky:
        type: "string"
      shared:
        type: "boolean"
      grant:
        type: "string"
      deletedDate:
        type: "string"
        format: "date-time"
      restoredDate:
        type: "string"
        format: "date-time"
      firstConnectionDate:
        type: "string"
        format: "date-time"
      isDeleted:
        type: "boolean"
      roleId:
        type: "integer"
        format: "int64"
      timezone:
        type: "string"
      availableConnectors:
        type: "array"
        items:
          type: "string"
          enum:
          - "Web"
          - "FacebookPage"
          - "FacebookGroup"
          - "Instagram"
          - "Twitter"
          - "Linkedin"
          - "Gmb"
          - "Pinterest"
          - "TikTok"
          - "TikTokBusiness"
          - "Youtube"
          - "Twitch"
          - "FacebookAds"
          - "GoogleAds"
          - "TikTokAds"
          - "FeedRss"
          - "Threads"
          - "Bluesky"
      brandRoleActionDefinitions:
        type: "array"
        items:
          type: "string"
          enum:
          - "VIEW_ALL_ANALYTICS"
          - "VIEW_INBOX"
          - "VIEW_PLANNER"
          - "VIEW_ADS"
          - "VIEW_SMARTLINKS"
          - "FULL_ACCESS_REPORTS"
          - "FULL_ACCESS_INBOX"
          - "FULL_ACCESS_PLANNER"
          - "FULL_ACCESS_ADS"
          - "FULL_ACCESS_SMARTLINKS"
          - "FULL_ACCESS_HASHTAG_TRACKER"
          - "EDIT_BRAND"
          - "SCHEDULE_POSTS"
          - "PUBLISH_POSTS"
          - "APPROVE_POSTS"
          - "VIEW_CONDENSED_ANALYTICS"
      readOnly:
        type: "boolean"
  GrantedAuthority:
    type: "object"
    properties:
      authority:
        type: "string"
  OnboardingName:
    type: "object"
    properties:
      name:
        type: "string"
  PartnerOnboardingProperties:
    type: "object"
    properties:
      name:
        $ref: "#/definitions/OnboardingName"
      finished:
        type: "boolean"
  Payment:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      externalId:
        type: "string"
      paymentId:
        type: "string"
      subscriptionId:
        type: "string"
      description:
        type: "string"
      date:
        type: "string"
        format: "date-time"
      amount:
        type: "number"
        format: "float"
      currency:
        type: "string"
      periodStart:
        type: "string"
        format: "date-time"
      periodEnd:
        type: "string"
        format: "date-time"
      eurRate:
        type: "number"
        format: "double"
      rateDate:
        type: "string"
        format: "date-time"
      invoiceNumber:
        type: "string"
      paymentType:
        type: "string"
      vatRate:
        type: "number"
        format: "double"
      company:
        type: "string"
      country:
        type: "string"
      state:
        type: "string"
      address:
        type: "string"
      vatNumber:
        type: "string"
      paymentToRefundId:
        type: "string"
      paymentToRefundInvoiceNumber:
        type: "string"
      paymentToRefundDate:
        type: "string"
        format: "date-time"
      sync:
        type: "boolean"
      netsuiteInternalId:
        type: "string"
      base:
        type: "number"
        format: "double"
      vat:
        type: "number"
        format: "double"
      errorDetail:
        type: "string"
      blogList:
        type: "array"
        items:
          $ref: "#/definitions/Blog"
      observations:
        type: "string"
      creditNote:
        type: "boolean"
      disbursement:
        type: "boolean"
  User:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      userName:
        type: "string"
      role:
        type: "string"
      enabled:
        type: "boolean"
      name:
        type: "string"
      lastName:
        type: "string"
      mail:
        type: "string"
      phone:
        type: "string"
      language:
        type: "string"
      timezone:
        type: "string"
      accountLogo:
        type: "string"
      headerLogo:
        type: "string"
      btCustomerId:
        type: "string"
      stripeCustomerId:
        type: "string"
      taxData:
        $ref: "#/definitions/TaxData"
      affiliated:
        type: "boolean"
      whiteLabel:
        type: "boolean"
      academic:
        type: "boolean"
      beta:
        type: "boolean"
      sendToAlternativeEmail:
        type: "boolean"
      alternativeEmail:
        type: "string"
      billEmails:
        type: "array"
        items:
          type: "string"
      marketingNotifications:
        type: "boolean"
      token:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      deleted:
        $ref: "#/definitions/DateTimeInfo"
      isDeleted:
        type: "boolean"
      locked:
        type: "boolean"
      changePasswordRequired:
        type: "boolean"
      onboarding:
        $ref: "#/definitions/OnboardingData"
      activeBrands:
        type: "integer"
        format: "int32"
      registeredFromTkAppCenter:
        type: "boolean"
      firstDayOfTheWeek:
        type: "integer"
        format: "int32"
      whiteLabelIntegrator:
        type: "boolean"
      requiresEmailAddress:
        type: "boolean"
      vendastaSettings:
        $ref: "#/definitions/VendastaData"
      crispWorkspaceId:
        type: "string"
      agencyCKId:
        type: "integer"
        format: "int32"
      integratedIn:
        type: "string"
      accountManagerMail:
        type: "string"
      passwordExpirationDate:
        $ref: "#/definitions/DateTimeInfo"
      blogId:
        type: "integer"
        format: "int32"
      customBrandMail:
        type: "string"
      brandLabel:
        type: "string"
  UserIdentifier:
    type: "object"
    properties:
      id:
        type: "object"
  UserSettings:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      name:
        type: "string"
      lastName:
        type: "string"
      mail:
        type: "string"
      language:
        type: "string"
      timezone:
        type: "string"
      company:
        type: "string"
      country:
        type: "string"
      state:
        type: "string"
      address:
        type: "string"
      vat:
        type: "string"
      subscription:
        $ref: "#/definitions/Subscription"
      payment:
        $ref: "#/definitions/Payment"
      whiteLabelSettings:
        $ref: "#/definitions/WhiteLabelSettings"
      sharedWithUser:
        type: "boolean"
      vendastaUser:
        type: "boolean"
      vendastaSettings:
        $ref: "#/definitions/VendastaData"
      hashtagBalance:
        type: "integer"
        format: "int32"
      vaxRate:
        type: "integer"
        format: "int32"
      activeBrands:
        type: "integer"
        format: "int32"
      whiteLabel:
        type: "boolean"
      beta:
        type: "boolean"
  VendastaData:
    type: "object"
    properties:
      accountId:
        type: "string"
      productNavBarDataUrl:
        type: "string"
  WhiteLabelSettings:
    type: "object"
    properties:
      iframeMode:
        type: "boolean"
      enabledChat:
        type: "boolean"
      footerLogo:
        type: "string"
      footerLegalUrl:
        type: "string"
      footerContactUrl:
        type: "string"
      footerTwitterUrl:
        type: "string"
      footerFacebookUrl:
        type: "string"
      footerInstagramUrl:
        type: "string"
      footerTiktokUrl:
        type: "string"
      footerYoutubeUrl:
        type: "string"
      footerPinterestUrl:
        type: "string"
      loginUrl:
        type: "string"
      hideMainMenu:
        type: "boolean"
      showAdsMenu:
        type: "boolean"
      showPlannerMenu:
        type: "boolean"
      showSmartLinksMenu:
        type: "boolean"
      showInboxMenu:
        type: "boolean"
      showEvolutionMenu:
        type: "boolean"
      showReportExample:
        type: "boolean"
      reportExamplePictureUrl:
        type: "string"
      showSubscriptionEmail:
        type: "boolean"
      showMessageBackground:
        type: "boolean"
      hideBrandedContent:
        type: "boolean"
      customizedCssUrl:
        type: "string"
      integratorKey:
        type: "string"
      colors:
        type: "object"
        additionalProperties:
          type: "string"
      reportBackgroundUrl:
        type: "string"
      reportBackgroundCoverUrl:
        type: "string"
      enabledReportTemplates:
        type: "boolean"
      customDomainBaseUrl:
        type: "string"
      customSmtpProperties:
        type: "object"
        additionalProperties:
          type: "string"
  SessionToken:
    type: "object"
    properties:
      code:
        type: "string"
  DatasetRequest:
    type: "object"
  DataStudioAd:
    type: "object"
    properties:
      adAccount:
        type: "string"
      customEventType:
        type: "string"
      objective:
        type: "string"
      provider:
        type: "string"
      providerCampaignId:
        type: "string"
      conversions:
        type: "number"
        format: "double"
      actions:
        type: "object"
        additionalProperties:
          type: "number"
          format: "double"
      campaignId:
        type: "string"
      campaignName:
        type: "string"
      adGroupId:
        type: "string"
      adgroupName:
        type: "string"
      adId:
        type: "string"
      adName:
        type: "string"
      imageUrl:
        type: "string"
      boostId:
        type: "string"
      currency:
        type: "string"
      metrics:
        type: "object"
        additionalProperties:
          type: "object"
          additionalProperties:
            type: "number"
            format: "double"
  JsonOkListResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          type: "object"
  JsonOkListResponseTimelineSeries:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/TimelineSeries"
  JsonPaging:
    type: "object"
    properties:
      next:
        type: "string"
  SeriesValue:
    type: "object"
    properties:
      dateTime:
        type: "string"
        format: "date-time"
      value:
        type: "number"
        format: "double"
  TimelineAggregate:
    type: "object"
    properties:
      aggregation:
        type: "string"
      value:
        type: "number"
        format: "double"
  TimelineSeries:
    type: "object"
    properties:
      metric:
        type: "string"
      values:
        type: "array"
        items:
          $ref: "#/definitions/SeriesValue"
      aggregate:
        $ref: "#/definitions/TimelineAggregate"
  Hashtag:
    type: "object"
    properties:
      name:
        type: "string"
      postsCount:
        type: "integer"
        format: "int64"
  JsonOkListResponseHashtag:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Hashtag"
  JsonOkResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "object"
  JsonOkResponseDouble:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "number"
        format: "double"
  BrandSummaryPost:
    type: "object"
    properties:
      id:
        type: "string"
      network:
        type: "string"
      text:
        type: "string"
      link:
        type: "string"
      picture:
        type: "string"
      publicationDate:
        $ref: "#/definitions/DateTimeInfo"
      metrics:
        type: "object"
        additionalProperties:
          type: "object"
  JsonOkListResponseBrandSummaryPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BrandSummaryPost"
  Campaign:
    type: "object"
    properties:
      network:
        type: "string"
      providerCampaignId:
        type: "string"
      name:
        type: "string"
      status:
        type: "string"
        enum:
        - "ACTIVE"
        - "PAUSED"
        - "REMOVED"
      objective:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      updated:
        $ref: "#/definitions/DateTimeInfo"
      start:
        $ref: "#/definitions/DateTimeInfo"
      stop:
        $ref: "#/definitions/DateTimeInfo"
      dailyBudget:
        type: "number"
        format: "double"
      lifetimeBudget:
        type: "number"
        format: "double"
      currency:
        type: "string"
      biddingStrategyType:
        type: "string"
      metrics:
        type: "object"
        additionalProperties:
          type: "object"
  JsonOkListResponseCampaign:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Campaign"
  DistributionItem:
    type: "object"
    properties:
      key:
        type: "string"
      value:
        type: "number"
        format: "double"
  JsonOkListResponseDistributionItem:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/DistributionItem"
  JsonOkResponseCollectionString:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          type: "string"
  JsonOkListResponseYoutubeCompetitor:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/YoutubeCompetitor"
  YoutubeCompetitor:
    type: "object"
    properties:
      channelId:
        type: "string"
      url:
        type: "string"
      fullName:
        type: "string"
      picture:
        type: "string"
  BlueskyCompetitor:
    type: "object"
    properties:
      did:
        type: "string"
      handle:
        type: "string"
      screenName:
        type: "string"
      picture:
        type: "string"
  JsonOkListResponseBlueskyCompetitor:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BlueskyCompetitor"
  BlueskyPost:
    type: "object"
    properties:
      postId:
        type: "string"
      mediaUrl:
        type: "string"
      providerUserId:
        type: "string"
      handle:
        type: "string"
      type:
        type: "string"
      text:
        type: "string"
      published:
        $ref: "#/definitions/DateTimeInfo"
      thumbnail:
        type: "string"
      likes:
        type: "integer"
        format: "int32"
      replies:
        type: "integer"
        format: "int32"
      reposts:
        type: "integer"
        format: "int32"
      quotes:
        type: "integer"
        format: "int32"
  JsonOkListResponseBlueskyPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BlueskyPost"
  BlueskyEvent:
    type: "object"
    properties:
      did:
        type: "string"
      date:
        type: "integer"
        format: "int32"
      screenName:
        type: "string"
      displayName:
        type: "string"
      picture:
        type: "string"
      profileUrl:
        type: "string"
      followers:
        type: "integer"
        format: "int64"
      isFollowedByMe:
        type: "boolean"
      isFollowingMe:
        type: "boolean"
  JsonOkResponseBoolean:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "boolean"
  Influencer:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      provider:
        type: "string"
      providerId:
        type: "string"
      screenName:
        type: "string"
      displayName:
        type: "string"
      picture:
        type: "string"
      cost:
        type: "number"
        format: "float"
      favorite:
        type: "boolean"
      costPer1kFollowers:
        type: "number"
        format: "double"
      costPerInteraction:
        type: "number"
        format: "double"
      updated:
        type: "string"
        format: "date-time"
      followers:
        type: "number"
        format: "double"
      following:
        type: "number"
        format: "double"
      posts:
        type: "integer"
        format: "int64"
      reels:
        type: "integer"
        format: "int64"
      likes:
        type: "number"
        format: "double"
      favorites:
        type: "number"
        format: "double"
      comments:
        type: "number"
        format: "double"
      reactions:
        type: "number"
        format: "double"
      shares:
        type: "number"
        format: "double"
      engagement:
        type: "number"
        format: "double"
      retweets:
        type: "number"
        format: "double"
      views:
        type: "number"
        format: "double"
      dislikes:
        type: "number"
        format: "double"
      totalViews:
        type: "number"
        format: "double"
      isDemo:
        type: "boolean"
      clips:
        type: "integer"
        format: "int64"
  JsonOkResponseInfluencer:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/Influencer"
  JsonOkListResponseInfluencer:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Influencer"
  InstagramCompetitorMedia:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      blogId:
        type: "integer"
        format: "int64"
      postId:
        type: "string"
      likes:
        type: "integer"
        format: "int32"
      comments:
        type: "integer"
        format: "int32"
      interactions:
        type: "integer"
        format: "int64"
      timestamp:
        type: "integer"
        format: "int64"
      created:
        type: "string"
      createdAt:
        $ref: "#/definitions/DateTimeInfo"
      filter:
        type: "string"
      url:
        type: "string"
      content:
        type: "string"
      imageUrl:
        type: "string"
      userId:
        type: "string"
      businessId:
        type: "string"
      hashtags:
        type: "array"
        items:
          type: "string"
      clicks:
        type: "number"
        format: "double"
      engagement:
        type: "number"
        format: "double"
      impressions:
        type: "integer"
        format: "int32"
      reach:
        type: "integer"
        format: "int32"
      saved:
        type: "integer"
        format: "int32"
      videoViews:
        type: "integer"
        format: "int32"
      followers:
        type: "integer"
        format: "int64"
      linkId:
        type: "integer"
        format: "int32"
      shortUrl:
        type: "string"
      type:
        type: "string"
      impressionsPaid:
        type: "integer"
        format: "int32"
      impressionsTotal:
        type: "integer"
        format: "int32"
      reachPaid:
        type: "integer"
        format: "int32"
      videoViewsPaid:
        type: "integer"
        format: "int32"
      videoViewsTotal:
        type: "integer"
        format: "int32"
      postClicksPaid:
        type: "integer"
        format: "int32"
      postInteractionsPaid:
        type: "integer"
        format: "int32"
      ownerScreenName:
        type: "string"
      ownerDisplayName:
        type: "string"
      ownerPicture:
        type: "string"
  JsonOkListResponseInstagramCompetitorMedia:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/InstagramCompetitorMedia"
  CompetitorTweet:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      id:
        type: "integer"
        format: "int64"
      idStr:
        type: "string"
      userId:
        type: "integer"
        format: "int64"
      createdAt:
        type: "string"
        format: "date-time"
      creationDate:
        $ref: "#/definitions/DateTimeInfo"
      text:
        type: "string"
      updatedAt:
        type: "string"
        format: "date-time"
      favoriteCount:
        type: "integer"
        format: "int32"
      retweetCount:
        type: "integer"
        format: "int32"
      linkClicks:
        type: "integer"
        format: "int32"
      promoted:
        type: "boolean"
      metricsV2:
        type: "object"
        additionalProperties:
          type: "object"
      userName:
        type: "string"
      screenName:
        type: "string"
      followers:
        type: "integer"
        format: "int64"
      impressions:
        type: "integer"
        format: "int64"
      imageUrl:
        type: "string"
      timestamp:
        type: "integer"
        format: "int64"
      source:
        type: "string"
      interactions:
        type: "integer"
        format: "int64"
      engagement:
        type: "number"
        format: "double"
      picture:
        type: "string"
      ownerPicture:
        type: "string"
      hasVideo:
        type: "boolean"
      hasPhoto:
        type: "boolean"
      hasUrls:
        type: "boolean"
      isRetweet:
        type: "boolean"
      inReplyToScreenName:
        type: "string"
      inReplyToStatusIdStr:
        type: "string"
      inReplyToStatusId:
        type: "integer"
        format: "int64"
      user:
        $ref: "#/definitions/TwitterProfile"
      retweetedStatus:
        $ref: "#/definitions/CompetitorTweet"
      entities:
        $ref: "#/definitions/TwitterEntities"
      extendedEntities:
        $ref: "#/definitions/TwitterExtendedEntities"
      coordinates:
        $ref: "#/definitions/TwitterCoordinates"
      created:
        type: "string"
        format: "date-time"
      retweets:
        type: "integer"
        format: "int32"
      favorites:
        type: "integer"
        format: "int32"
      retweet:
        type: "boolean"
      tweetId:
        type: "string"
      hasMedia:
        type: "boolean"
      hasTags:
        type: "boolean"
      lang:
        type: "string"
  JsonOkListResponseCompetitorTweet:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/CompetitorTweet"
  FacebookCompetitorPost:
    type: "object"
    properties:
      pageId:
        type: "string"
      postId:
        type: "string"
      created:
        type: "string"
        format: "date-time"
      creationDate:
        $ref: "#/definitions/DateTimeInfo"
      timestamp:
        type: "integer"
        format: "int64"
      link:
        type: "string"
      text:
        type: "string"
      type:
        type: "string"
      shares:
        type: "integer"
        format: "int32"
      comments:
        type: "integer"
        format: "int32"
      reactions:
        type: "integer"
        format: "int32"
      impressions:
        type: "integer"
        format: "int32"
      impressionsPaid:
        type: "integer"
        format: "int32"
      impressionsOrganic:
        type: "integer"
        format: "int32"
      impressionsUnique:
        type: "integer"
        format: "int32"
      impressionsUniquePaid:
        type: "integer"
        format: "int32"
      impressionsUniqueOrganic:
        type: "integer"
        format: "int32"
      clicks:
        type: "integer"
        format: "int32"
      engagement:
        type: "number"
        format: "double"
      picture:
        type: "string"
      videoViews:
        type: "integer"
        format: "int32"
      videoViewsPaid:
        type: "integer"
        format: "int32"
      videoViewsOrganic:
        type: "integer"
        format: "int32"
      videoTimeWatched:
        type: "integer"
        format: "int32"
      linkclicks:
        type: "integer"
        format: "int32"
      spend:
        type: "number"
        format: "double"
      ownerScreenName:
        type: "string"
      ownerDisplayName:
        type: "string"
      ownerPicture:
        type: "string"
  JsonOkListResponseFacebookCompetitorPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/FacebookCompetitorPost"
  CompetitorTwitchVideo:
    type: "object"
    properties:
      channelId:
        type: "string"
      videoId:
        type: "string"
      thumbnailUrl:
        type: "string"
      videoUrl:
        type: "string"
      title:
        type: "string"
      created:
        type: "string"
        format: "date-time"
      createdAt:
        $ref: "#/definitions/DateTimeInfo"
      createdAtTimestamp:
        $ref: "#/definitions/DateTimeInfo"
      game:
        type: "string"
      duration:
        type: "number"
        format: "double"
      views:
        type: "number"
        format: "double"
      averageViews:
        type: "number"
        format: "double"
      clips:
        type: "integer"
        format: "int32"
      clipId:
        type: "string"
      clipUrl:
        type: "string"
      videoNameForClip:
        type: "string"
      videoUrlForClip:
        type: "string"
      ownerScreenName:
        type: "string"
      ownerDisplayName:
        type: "string"
      ownerPicture:
        type: "string"
  JsonOkListResponseCompetitorTwitchVideo:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/CompetitorTwitchVideo"
  CompetitorTwitchClip:
    type: "object"
    properties:
      channelId:
        type: "string"
      videoId:
        type: "string"
      clipId:
        type: "string"
      thumbnailUrl:
        type: "string"
      clipUrl:
        type: "string"
      title:
        type: "string"
      created:
        type: "string"
        format: "date-time"
      createdAt:
        $ref: "#/definitions/DateTimeInfo"
      createdAtTimestamp:
        $ref: "#/definitions/DateTimeInfo"
      game:
        type: "string"
      views:
        type: "number"
        format: "double"
      ownerScreenName:
        type: "string"
      ownerDisplayName:
        type: "string"
      ownerPicture:
        type: "string"
  JsonOkListResponseCompetitorTwitchClip:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/CompetitorTwitchClip"
  JsonOkListResponseYouTubeCompetitorVideo:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/YouTubeCompetitorVideo"
  YouTubeCompetitorVideo:
    type: "object"
    properties:
      videoId:
        type: "string"
      thumbnailUrl:
        type: "string"
      title:
        type: "string"
      description:
        type: "string"
      publishedAt:
        type: "integer"
        format: "int64"
      publishedDate:
        $ref: "#/definitions/DateTimeInfo"
      views:
        type: "number"
        format: "double"
      watchMinutes:
        type: "number"
        format: "double"
      averageViewDuration:
        type: "number"
        format: "double"
      likes:
        type: "number"
        format: "double"
      dislikes:
        type: "number"
        format: "double"
      comments:
        type: "number"
        format: "double"
      shares:
        type: "number"
        format: "double"
      estimatedRedPartnerRevenue:
        type: "number"
        format: "double"
      estimatedAdRevenue:
        type: "number"
        format: "double"
      adImpressions:
        type: "number"
        format: "double"
      monetizedPlaybacks:
        type: "number"
        format: "double"
      ownerScreenName:
        type: "string"
      ownerDisplayName:
        type: "string"
      ownerPicture:
        type: "string"
      channelId:
        type: "string"
      hasRevenueData:
        type: "boolean"
      watchUrl:
        type: "string"
      formattedAvgViewDuration:
        type: "string"
      formattedWatchTime:
        type: "string"
  BlueskyCompetitorPost:
    type: "object"
    properties:
      avatar:
        type: "string"
      displayName:
        type: "string"
      postId:
        type: "string"
      mediaUrl:
        type: "string"
      providerUserId:
        type: "string"
      handle:
        type: "string"
      type:
        type: "string"
      text:
        type: "string"
      published:
        $ref: "#/definitions/DateTimeInfo"
      thumbnail:
        type: "string"
      likes:
        type: "integer"
        format: "int32"
      replies:
        type: "integer"
        format: "int32"
      reposts:
        type: "integer"
        format: "int32"
      quotes:
        type: "integer"
        format: "int32"
  JsonOkListResponseBlueskyCompetitorPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BlueskyCompetitorPost"
  JsonOkListResponseFacebookPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/FacebookPost"
  FacebookReel:
    type: "object"
    properties:
      pageId:
        type: "string"
      reelId:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      description:
        type: "string"
      videoUrl:
        type: "string"
      length:
        type: "number"
        format: "double"
      thumbnailUrl:
        type: "string"
      reelUrl:
        type: "string"
      blueReelsPlayCount:
        type: "integer"
        format: "int32"
      postImpressionsUnique:
        type: "integer"
        format: "int32"
      postVideoAvgTimeWatchedSeconds:
        type: "number"
        format: "double"
      postVideoViewTimeSeconds:
        type: "number"
        format: "double"
      postVideoReactions:
        type: "integer"
        format: "int32"
      postVideoSocialActions:
        type: "integer"
        format: "int32"
      engagement:
        type: "number"
        format: "double"
  JsonOkListResponseFacebookReel:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/FacebookReel"
  FacebookStory:
    type: "object"
    properties:
      pageId:
        type: "string"
      storyId:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      mediaType:
        type: "string"
      mediaId:
        type: "string"
      storyUrl:
        type: "string"
      thumbnailUrl:
        type: "string"
  JsonOkListResponseFacebookStory:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/FacebookStory"
  GbpKeyword:
    type: "object"
    properties:
      keyword:
        type: "string"
      value:
        type: "number"
        format: "double"
  JsonOkListResponseGbpKeyword:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/GbpKeyword"
  HashtagsTrackerSession:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      blogId:
        type: "integer"
        format: "int32"
      hash:
        type: "string"
      start:
        $ref: "#/definitions/DateTimeInfo"
      end:
        $ref: "#/definitions/DateTimeInfo"
      createdAt:
        $ref: "#/definitions/DateTimeInfo"
      consolidatedDateTime:
        $ref: "#/definitions/DateTimeInfo"
      consolidated:
        type: "boolean"
      scanned:
        type: "boolean"
      duration:
        type: "integer"
        format: "int32"
      query:
        type: "string"
      tweetsCount:
        type: "integer"
        format: "int32"
      igPostsCount:
        type: "integer"
        format: "int32"
      logo:
        type: "string"
      enabledNetworks:
        type: "array"
        items:
          type: "string"
      manualConsolidationTodayCounter:
        type: "integer"
        format: "int32"
  JsonOkResponseHashtagsTrackerSession:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/HashtagsTrackerSession"
  TrackSessionRequest:
    type: "object"
    required:
    - "duration"
    - "start"
    properties:
      start:
        $ref: "#/definitions/DateTimeInfo"
      duration:
        type: "integer"
        format: "int32"
      query:
        type: "string"
      networks:
        type: "array"
        items:
          type: "string"
  JsonOkResponsePurchaseDaysResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/PurchaseDaysResponse"
  PurchaseDaysResponse:
    type: "object"
    properties:
      status:
        type: "string"
      paymentProvider:
        type: "string"
      paymentMethodId:
        type: "string"
      numOfDays:
        type: "integer"
        format: "int32"
      currency:
        type: "string"
      additionalInformationFromProvider:
        type: "object"
        additionalProperties:
          type: "object"
  PurchaseDaysRequest:
    type: "object"
    required:
    - "currency"
    - "numOfDays"
    properties:
      paymentProvider:
        type: "string"
      paymentMethodId:
        type: "string"
      numOfDays:
        type: "integer"
        format: "int32"
      currency:
        type: "string"
  JsonOkListResponseHashtagsTrackerSession:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/HashtagsTrackerSession"
  InstagramHashtag:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      hashtag:
        type: "string"
      impressions:
        type: "integer"
        format: "int32"
      views:
        type: "integer"
        format: "int32"
      count:
        type: "integer"
        format: "int32"
      likes:
        type: "integer"
        format: "int32"
      commentsCount:
        type: "integer"
        format: "int32"
      posts:
        type: "array"
        items:
          $ref: "#/definitions/InstagramPost"
  JsonOkListResponseInstagramHashtag:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/InstagramHashtag"
  JsonOkListResponseInstagramReel:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/InstagramReel"
  JsonOkListResponseInstagramPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/InstagramPost"
  JsonOkListResponseInstagramStory:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/InstagramStory"
  JsonOkListResponseLinkedinPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/LinkedinPost"
  Photo:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      width:
        type: "integer"
        format: "int32"
      height:
        type: "integer"
        format: "int32"
      url:
        type: "string"
      photographer:
        type: "string"
      photographerUrl:
        type: "string"
      photographerId:
        type: "string"
      avgColor:
        type: "string"
      src:
        $ref: "#/definitions/Src"
      alt:
        type: "string"
  PhotosSearchResponse:
    type: "object"
    properties:
      photos:
        type: "array"
        items:
          $ref: "#/definitions/Photo"
      page:
        type: "integer"
        format: "int32"
      perPage:
        type: "integer"
        format: "int32"
      totalResults:
        type: "integer"
        format: "int32"
      prevPage:
        type: "string"
      nextPage:
        type: "string"
  Src:
    type: "object"
    properties:
      original:
        type: "string"
      large:
        type: "string"
      medium:
        type: "string"
      small:
        type: "string"
  Video:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      width:
        type: "integer"
        format: "int32"
      height:
        type: "integer"
        format: "int32"
      url:
        type: "string"
      image:
        type: "string"
      duration:
        type: "integer"
        format: "int32"
      user:
        $ref: "#/definitions/User"
      videoFiles:
        type: "array"
        items:
          $ref: "#/definitions/VideoFile"
  VideoFile:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      quality:
        type: "string"
      fileType:
        type: "string"
      width:
        type: "integer"
        format: "int32"
      height:
        type: "integer"
        format: "int32"
      fps:
        type: "number"
        format: "double"
      link:
        type: "string"
  VideosSearchResponse:
    type: "object"
    properties:
      videos:
        type: "array"
        items:
          $ref: "#/definitions/Video"
      page:
        type: "integer"
        format: "int32"
      perPage:
        type: "integer"
        format: "int32"
      totalResults:
        type: "integer"
        format: "int64"
      prevPage:
        type: "string"
      nextPage:
        type: "string"
  JsonOkResponseUploadMediaResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/UploadMediaResponse"
  UploadMediaResponse:
    type: "object"
    properties:
      url:
        type: "string"
  ChunkOptions:
    type: "object"
    properties:
      chunkUrls:
        type: "array"
        items:
          type: "string"
        maxItems: 2147483647
        minItems: 2
      hash:
        type: "string"
  MergeMediaRequest:
    type: "object"
    required:
    - "chunkOptions"
    properties:
      chunkOptions:
        $ref: "#/definitions/ChunkOptions"
      transformOptions:
        $ref: "#/definitions/TransformOptions"
      folder:
        type: "string"
      mergedFileName:
        type: "string"
      transformEngine:
        type: "string"
  TransformOptions:
    type: "object"
    properties:
      sourceFormat:
        type: "string"
      targetFormat:
        type: "string"
      engine:
        type: "string"
  JsonOkListResponsePin:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Pin"
  Pin:
    type: "object"
    properties:
      accountId:
        type: "string"
      id:
        type: "string"
      createdAt:
        type: "string"
        format: "date-time"
      link:
        type: "string"
      title:
        type: "string"
      description:
        type: "string"
      altText:
        type: "string"
      boardId:
        type: "string"
      boardSectionId:
        type: "string"
      boardOwner:
        type: "string"
      mediaType:
        type: "string"
      imageUrl:
        type: "string"
      impressions:
        type: "integer"
        format: "int32"
      saves:
        type: "integer"
        format: "int32"
      pinClicks:
        type: "integer"
        format: "int32"
      outboundClicks:
        type: "integer"
        format: "int32"
      videoMrcViews:
        type: "integer"
        format: "int32"
      videoAvgWatchTime:
        type: "integer"
        format: "int32"
      videoV50WatchTime:
        type: "number"
        format: "double"
      quartile95PercentViews:
        type: "number"
        format: "double"
  Button:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      deleted:
        type: "boolean"
      shortener:
        type: "string"
      destination:
        type: "string"
      disabled:
        type: "boolean"
      type:
        type: "string"
      background:
        type: "string"
      color:
        type: "string"
      text:
        type: "string"
      border:
        type: "string"
  Content:
    type: "object"
    properties:
      icons:
        type: "array"
        items:
          $ref: "#/definitions/Icon"
      buttons:
        type: "array"
        items:
          $ref: "#/definitions/Button"
      images:
        type: "array"
        items:
          $ref: "#/definitions/Image"
      header:
        $ref: "#/definitions/Header"
  Header:
    type: "object"
    properties:
      title:
        type: "string"
      subtitle:
        type: "string"
      imageUrl:
        type: "string"
  Icon:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      deleted:
        type: "boolean"
      shortener:
        type: "string"
      destination:
        type: "string"
      disabled:
        type: "boolean"
      icon:
        type: "string"
  Image:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      deleted:
        type: "boolean"
      shortener:
        type: "string"
      destination:
        type: "string"
      disabled:
        type: "boolean"
      provider:
        type: "string"
      providerId:
        type: "string"
      src:
        type: "string"
      creationDate:
        type: "string"
        format: "date-time"
  JsonOkResponseSmartLink:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/SmartLink"
  SmartLink:
    type: "object"
    properties:
      appearance:
        type: "object"
        additionalProperties:
          type: "object"
      id:
        type: "integer"
        format: "int64"
      slug:
        type: "string"
      name:
        type: "string"
      content:
        $ref: "#/definitions/Content"
      version:
        type: "integer"
        format: "int32"
      free:
        type: "boolean"
  ButtonRow:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      button:
        $ref: "#/definitions/ContentItem"
      clicks:
        type: "number"
        format: "double"
      ctr:
        type: "number"
        format: "double"
  ContentItem:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      deleted:
        type: "boolean"
      shortener:
        type: "string"
      destination:
        type: "string"
      disabled:
        type: "boolean"
  JsonOkListResponseButtonRow:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ButtonRow"
  JsonOkResponseString:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "string"
  ImageRow:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      image:
        $ref: "#/definitions/Image"
      clicks:
        type: "number"
        format: "double"
      ctr:
        type: "number"
        format: "double"
  JsonOkListResponseImageRow:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ImageRow"
  JsonOkListResponseSmartLink:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/SmartLink"
  JsonOkListResponseThreadsPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ThreadsPost"
  ThreadsPost:
    type: "object"
    properties:
      providerUserId:
        type: "string"
      publishedDate:
        $ref: "#/definitions/DateTimeInfo"
      id:
        type: "string"
      text:
        type: "string"
      mediaUrl:
        type: "string"
      mediaType:
        type: "string"
      thumbnailUrl:
        type: "string"
      owner:
        type: "string"
      shortCode:
        type: "string"
      isQuotePost:
        type: "boolean"
      permalink:
        type: "string"
      views:
        type: "integer"
        format: "int32"
      likes:
        type: "integer"
        format: "int32"
      replies:
        type: "integer"
        format: "int32"
      reposts:
        type: "integer"
        format: "int32"
      quotes:
        type: "integer"
        format: "int32"
  JsonOkListResponseTikTokPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/TikTokPost"
  TikTokPost:
    type: "object"
    properties:
      openId:
        type: "string"
      videoId:
        type: "string"
      type:
        type: "string"
      createTime:
        type: "string"
        format: "date-time"
      coverImageUrl:
        type: "string"
      shareUrl:
        type: "string"
      videoDescription:
        type: "string"
      duration:
        type: "integer"
        format: "int32"
      height:
        type: "integer"
        format: "int32"
      width:
        type: "integer"
        format: "int32"
      title:
        type: "string"
      embedLink:
        type: "string"
      likeCount:
        type: "integer"
        format: "int32"
      commentCount:
        type: "integer"
        format: "int32"
      shareCount:
        type: "integer"
        format: "int32"
      viewCount:
        type: "integer"
        format: "int64"
      engagement:
        type: "number"
        format: "double"
      reach:
        type: "integer"
        format: "int32"
      fullVideoWatchedRate:
        type: "number"
        format: "double"
      totalTimeWatched:
        type: "number"
        format: "double"
      averageTimeWatched:
        type: "number"
        format: "double"
      impressionSources:
        $ref: "#/definitions/TikTokVideoImpressionSources"
  TikTokVideoImpressionSources:
    type: "object"
    properties:
      forYou:
        type: "number"
        format: "double"
      follow:
        type: "number"
        format: "double"
      hashtag:
        type: "number"
        format: "double"
      sound:
        type: "number"
        format: "double"
      personalProfile:
        type: "number"
        format: "double"
      search:
        type: "number"
        format: "double"
  Adgroup:
    type: "object"
    properties:
      network:
        type: "string"
      campaignId:
        type: "string"
      campaignName:
        type: "string"
      providerAdgroupId:
        type: "string"
      name:
        type: "string"
      status:
        type: "string"
        enum:
        - "ACTIVE"
        - "PAUSED"
        - "REMOVED"
      dailyBudget:
        type: "number"
        format: "double"
      lifetimeBudget:
        type: "number"
        format: "double"
      currency:
        type: "string"
      biddingStrategyType:
        type: "string"
      maxCPC:
        type: "number"
        format: "double"
      metrics:
        type: "object"
        additionalProperties:
          type: "object"
  JsonOkListResponseAdgroup:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Adgroup"
  JsonOkListResponseAd:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Ad"
  AdPreview:
    type: "object"
    properties:
      previewUrl:
        type: "string"
  JsonOkResponseAdPreview:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/AdPreview"
  AdPlatformInfo:
    type: "object"
    required:
    - "platformId"
    properties:
      platformId:
        type: "string"
      objective:
        type: "string"
      displaySites:
        type: "array"
        items:
          type: "string"
      interests:
        type: "array"
        items:
          type: "string"
      keywords:
        type: "array"
        items:
          type: "string"
      dsaPayor:
        type: "string"
      dsaBeneficiary:
        type: "string"
      pixel:
        type: "string"
      customEvent:
        type: "string"
  CampaignCreationState:
    type: "object"
    properties:
      name:
        type: "string"
      targetUrl:
        type: "string"
      startDate:
        $ref: "#/definitions/DateTimeInfo"
      endDate:
        $ref: "#/definitions/DateTimeInfo"
      currency:
        type: "string"
      budget:
        type: "number"
      budgetType:
        type: "string"
      bidStrategy:
        type: "string"
      targetCPA:
        type: "number"
      maxCPC:
        type: "number"
      providers:
        type: "array"
        items:
          $ref: "#/definitions/AdPlatformInfo"
      segmentation:
        $ref: "#/definitions/Segmentation"
      ads:
        type: "array"
        items:
          $ref: "#/definitions/Ad"
      googleAdsData:
        $ref: "#/definitions/GoogleAdsData"
  GoogleAdsData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
  Location:
    type: "object"
    properties:
      id:
        type: "string"
      name:
        type: "string"
      type:
        type: "string"
  MediaItem:
    type: "object"
    properties:
      url:
        type: "string"
      mediaType:
        type: "string"
      width:
        type: "string"
      height:
        type: "string"
  Segmentation:
    type: "object"
    properties:
      ageRanges:
        type: "array"
        items:
          type: "string"
      gender:
        type: "string"
      language:
        type: "string"
      locations:
        type: "array"
        items:
          $ref: "#/definitions/Location"
  FbAdsAccountData:
    type: "object"
    properties:
      currency:
        type: "string"
      defaultDsaBeneficiary:
        type: "string"
      defaultDsaPayer:
        type: "string"
  JsonOkResponseFbAdsAccountData:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/FbAdsAccountData"
  JsonOkListResponseKeyword:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Keyword"
  Keyword:
    type: "object"
    properties:
      name:
        type: "string"
      composedName:
        type: "string"
      matchType:
        type: "string"
        enum:
        - "BROAD"
        - "EXACT"
        - "PHRASE"
        - "UNSPECIFIED"
        - "UNKNOWN"
      currency:
        type: "string"
      campaignName:
        type: "string"
      adGroupName:
        type: "string"
      qualityScore:
        type: "integer"
        format: "int32"
      searchScore:
        type: "integer"
        format: "int32"
      creativityScore:
        type: "integer"
        format: "int32"
      landingScore:
        type: "integer"
        format: "int32"
      metrics:
        type: "object"
        additionalProperties:
          type: "object"
  AdRecommendation:
    type: "object"
    properties:
      id:
        type: "string"
      type:
        type: "string"
        enum:
        - "CAMPAIGN_BUDGET"
        - "KEYWORD"
        - "TEXT_AD"
        - "TARGET_CPA_OPT_IN"
        - "MAXIMIZE_CONVERSIONS_OPT_IN"
        - "ENHANCED_CPC_OPT_IN"
        - "SEARCH_PARTNERS_OPT_IN"
        - "MAXIMIZE_CLICKS_OPT_IN"
        - "OPTIMIZE_AD_ROTATION"
        - "CALLOUT_ASSET"
        - "SITELINK_ASSET"
        - "CALL_ASSET"
        - "USE_BROAD_MATCH_KEYWORD"
        - "MOVE_UNUSED_BUDGET"
      campaignId:
        type: "string"
      campaignName:
        type: "string"
      dismissed:
        type: "boolean"
      currency:
        type: "string"
      details:
        type: "object"
        additionalProperties:
          type: "object"
  JsonOkResponseRecommendationsResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/RecommendationsResponse"
  RecommendationsResponse:
    type: "object"
    properties:
      summary:
        $ref: "#/definitions/Summary"
      recommendations:
        type: "array"
        items:
          $ref: "#/definitions/AdRecommendation"
  Summary:
    type: "object"
    properties:
      numOfRecommendations:
        type: "integer"
        format: "int32"
      clicks:
        type: "number"
        format: "double"
      impressions:
        type: "number"
        format: "double"
      conversions:
        type: "number"
        format: "double"
  ApplyRecommendationResult:
    type: "object"
    properties:
      recommendationId:
        type: "string"
      status:
        type: "string"
      detail:
        type: "string"
  JsonOkListResponseApplyRecommendationResult:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ApplyRecommendationResult"
  JsonOkListResponseSuggestedItem:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/SuggestedItem"
  SuggestedItem:
    type: "object"
    properties:
      network:
        type: "string"
      id:
        type: "string"
      label:
        type: "string"
  JsonOkListResponseSuggestedLocation:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/SuggestedLocation"
  SuggestedLocation:
    type: "object"
    properties:
      id:
        type: "string"
      name:
        type: "string"
      type:
        type: "string"
      countryCode:
        type: "string"
  JsonOkResponseLanguagesSuggestionResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/LanguagesSuggestionResponse"
  Language:
    type: "object"
    properties:
      id:
        type: "string"
      name:
        type: "string"
      label:
        type: "string"
  LanguagesSuggestionResponse:
    type: "object"
    properties:
      defaultLanguageId:
        type: "string"
      languages:
        type: "array"
        items:
          $ref: "#/definitions/Language"
  AudienceForecast:
    type: "object"
    properties:
      network:
        type: "string"
      min:
        type: "integer"
        format: "int64"
      max:
        type: "integer"
        format: "int64"
  JsonOkListResponseAudienceForecast:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/AudienceForecast"
  JsonOkListResponsePixel:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Pixel"
  Pixel:
    type: "object"
    properties:
      network:
        type: "string"
      id:
        type: "string"
      name:
        type: "string"
  AdsCustomEvent:
    type: "object"
    properties:
      network:
        type: "string"
      id:
        type: "string"
      name:
        type: "string"
      customEventType:
        type: "string"
      pixelId:
        type: "string"
  JsonOkListResponseAdsCustomEvent:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/AdsCustomEvent"
  JsonOkListResponsePlatformCurrency:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/PlatformCurrency"
  PlatformCurrency:
    type: "object"
    properties:
      network:
        type: "string"
      currency:
        type: "string"
  AgencyTestMailData:
    type: "object"
    properties:
      to:
        type: "string"
  AgencyDetailsDto:
    type: "object"
    properties:
      agencyId:
        type: "integer"
        format: "int32"
      name:
        type: "string"
      agencyLogo:
        type: "string"
      loginLogo:
        type: "string"
      supportChat:
        type: "boolean"
      helpArticles:
        type: "boolean"
      colorPalette:
        $ref: "#/definitions/ColorsDto"
  ColorsDto:
    type: "object"
    properties:
      blue:
        type: "string"
      teal:
        type: "string"
      pink:
        type: "string"
      yellow:
        type: "string"
      lightYellow:
        type: "string"
      darkYellow:
        type: "string"
      purple:
        type: "string"
      cyan:
        type: "string"
      red:
        type: "string"
      green:
        type: "string"
      slate:
        type: "string"
      charcoal:
        type: "string"
      cobalt:
        type: "string"
  JsonOkResponseAgencyDetailsDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/AgencyDetailsDto"
  AgencyDto:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      ownerId:
        type: "integer"
        format: "int32"
      domain:
        type: "string"
      loginUrl:
        type: "string"
      name:
        type: "string"
      enabled:
        type: "boolean"
      properties:
        $ref: "#/definitions/AgencyPropertiesDto"
  AgencyPropertiesDto:
    type: "object"
    properties:
      agencyLogo:
        type: "string"
      loginLogo:
        type: "string"
      supportChat:
        type: "boolean"
      helpArticles:
        type: "boolean"
      colorPalette:
        $ref: "#/definitions/ColorsDto"
      reportLogo:
        type: "string"
      mailMessage:
        type: "string"
      mailReplyTo:
        type: "string"
      mailLogo:
        type: "string"
      smtpConfiguration:
        $ref: "#/definitions/CustomSMTPPropertiesDto"
  CustomSMTPPropertiesDto:
    type: "object"
    properties:
      host:
        type: "string"
      port:
        type: "string"
      user:
        type: "string"
      password:
        type: "string"
      from:
        type: "string"
      auth:
        type: "string"
      quitwait:
        type: "string"
      debug:
        type: "string"
      from.label:
        type: "string"
        readOnly: true
      socketFactory.class:
        type: "string"
        readOnly: true
      socketFactory.port:
        type: "string"
        readOnly: true
      starttls.enable:
        type: "string"
        readOnly: true
      ssl.protocols:
        type: "string"
        readOnly: true
      ssl.trust:
        type: "string"
        readOnly: true
  JsonOkResponseAgencyDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/AgencyDto"
  AgencyPropertiesForUpdateDto:
    type: "object"
    properties:
      agencyLogo:
        type: "string"
      loginLogo:
        type: "string"
      supportChat:
        type: "boolean"
      helpArticles:
        type: "boolean"
      colorPalette:
        $ref: "#/definitions/ColorsDto"
      reportLogo:
        type: "string"
      mailMessage:
        type: "string"
      mailReplyTo:
        type: "string"
      mailLogo:
        type: "string"
  JsonOkResponseAgencyPropertiesForUpdateDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/AgencyPropertiesForUpdateDto"
  AgencyEndClientBrandDto:
    type: "object"
    required:
    - "brandId"
    - "enabled"
    - "roleId"
    properties:
      id:
        type: "integer"
        format: "int64"
      agencyId:
        type: "integer"
        format: "int32"
      endClientId:
        type: "integer"
        format: "int32"
      brandId:
        type: "integer"
        format: "int32"
      email:
        type: "string"
      enabled:
        type: "boolean"
      roleId:
        type: "integer"
        format: "int64"
      brandName:
        type: "string"
      roleName:
        type: "string"
  JsonOkListResponseAgencyEndClientBrandDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/AgencyEndClientBrandDto"
  AgencyEndClientActivationLinkRequest:
    type: "object"
    properties:
      invitationCustomMessage:
        type: "string"
  AgencyEndClientDto:
    type: "object"
    required:
    - "agencyId"
    - "id"
    - "username"
    properties:
      id:
        type: "integer"
        format: "int32"
      agencyId:
        type: "integer"
        format: "int32"
      username:
        type: "string"
      name:
        type: "string"
      lastname:
        type: "string"
      email:
        type: "string"
      language:
        type: "string"
      timezone:
        type: "string"
      enabled:
        type: "boolean"
      lastInvitationDate:
        $ref: "#/definitions/DateTimeInfo"
      assignments:
        type: "array"
        items:
          $ref: "#/definitions/AgencyEndClientBrandDto"
  JsonOkListResponseAgencyEndClientDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/AgencyEndClientDto"
  JsonOkResponseAgencyEndClientDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/AgencyEndClientDto"
  AgencyEndClientCreationRequest:
    type: "object"
    required:
    - "endClient"
    properties:
      endClient:
        $ref: "#/definitions/AgencyEndClientForCreationDto"
      mailMessage:
        type: "string"
  AgencyEndClientForCreationDto:
    type: "object"
    required:
    - "agencyId"
    - "username"
    properties:
      agencyId:
        type: "integer"
        format: "int32"
      username:
        type: "string"
      name:
        type: "string"
      lastname:
        type: "string"
      email:
        type: "string"
      language:
        type: "string"
      timezone:
        type: "string"
      enabled:
        type: "boolean"
      lastInvitationDate:
        $ref: "#/definitions/DateTimeInfo"
      assignments:
        type: "array"
        items:
          $ref: "#/definitions/AgencyEndClientBrandDto"
  JsonOkListResponseTeamMemberRoleDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/TeamMemberRoleDto"
  TeamMemberRoleActionDto:
    type: "object"
    properties:
      index:
        type: "integer"
        format: "int32"
        example: 1
        description: "Index of the action in the list"
      action:
        type: "string"
        example: "manageTeamMembers"
        description: "Name of the action"
      allowed:
        type: "boolean"
        example: true
        description: "Indicates if the action is allowed"
    description: "Information of a team member role action"
  TeamMemberRoleDto:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
        example: 1
        description: "Unique identifier of the team member role"
      name:
        type: "string"
        example: "Administrator"
        description: "Name of the team member role"
      description:
        type: "string"
        example: "Role with full access to all features"
        description: "Description of the team member role"
      actions:
        type: "array"
        description: "List of actions associated with the team member role"
        items:
          $ref: "#/definitions/TeamMemberRoleActionDto"
    description: "Information of a team member role"
  JsonOkListResponseTeamMemberDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/TeamMemberDto"
  TeamMemberDto:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
        example: 12345
        description: "Team Member ID"
      agencyId:
        type: "integer"
        format: "int32"
        example: 67890
        description: "Agency ID the team member belongs to"
      userId:
        type: "integer"
        format: "int32"
        example: 54321
        description: "User ID associated with the team member"
      email:
        type: "string"
        example: "teamMember1@myCompany.com"
        description: "Team member email"
      enabled:
        type: "boolean"
        example: true
        description: "Indicates if the team member is enabled"
      teamMemberRoleId:
        type: "integer"
        format: "int64"
        example: 1
        description: "Team Member Role ID assigned to the team member"
      lastInvitationSent:
        example: "{\"dateTime\":\"2023-10-05T14:48:00\",\"timeZone\":\"UTC\"}"
        description: "Information about the last invitation sent to the team member"
        $ref: "#/definitions/DateTimeInfo"
    description: "DTO for Team Member information"
  AgencyTeamMembersCreationRequest:
    type: "object"
    required:
    - "emails"
    - "roleId"
    properties:
      emails:
        type: "array"
        example: "[\"teammember1@metricoolcom\",\"teammember2@metricoolcom\"]"
        description: "List of emails for the new team members"
        items:
          type: "string"
      roleId:
        type: "integer"
        format: "int64"
        example: 1
        description: "Team Member Role ID to assign to the new team members"
    description: "Request to create a new Agency Team Member"
  JsonOkListResponseString:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          type: "string"
  EmailActivationInfo:
    type: "object"
    required:
    - "isDefaultEmail"
    properties:
      isDefaultEmail:
        type: "boolean"
      invitationCustomMessage:
        type: "string"
      useNewActivationLink:
        type: "boolean"
  BrandRoleAssignment:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      blogId:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      email:
        type: "string"
      blogName:
        type: "string"
      enabled:
        type: "boolean"
      roleId:
        type: "integer"
        format: "int64"
      roleName:
        type: "string"
  BrandRoleCollaborator:
    type: "object"
    properties:
      userId:
        type: "integer"
        format: "int32"
      email:
        type: "string"
      fullName:
        type: "string"
      isUserActive:
        type: "boolean"
      lastSent:
        $ref: "#/definitions/DateTimeInfo"
      assignments:
        type: "array"
        items:
          $ref: "#/definitions/BrandRoleAssignment"
  JsonOkListResponseBrandRoleCollaborator:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BrandRoleCollaborator"
  JsonOkResponseBrandRoleCollaborator:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/BrandRoleCollaborator"
  BrandRoleAssignmentsRequest:
    type: "object"
    properties:
      isDefaultEmail:
        type: "boolean"
      invitationCustomMessage:
        type: "string"
      assignments:
        type: "array"
        items:
          $ref: "#/definitions/BrandRoleAssignment"
      useNewActivationLink:
        type: "boolean"
  JsonOkListResponseBrandRoleAssignment:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BrandRoleAssignment"
  JsonOkListResponseBrandRole:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BrandRole"
  JsonOkResponseBrandRole:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/BrandRole"
  CreateBrandRoleRequest:
    type: "object"
    required:
    - "actions"
    properties:
      name:
        type: "string"
      description:
        type: "string"
      color:
        type: "string"
      actions:
        $ref: "#/definitions/BrandRoleActions"
  UpdateBrandRoleRequest:
    type: "object"
    properties:
      name:
        type: "string"
      description:
        type: "string"
      color:
        type: "string"
      actions:
        $ref: "#/definitions/BrandRoleActions"
  ChatResponse:
    type: "object"
    properties:
      sessionId:
        type: "string"
        example: "8d672794-d321-48d7-82a6-69fa78cebb00"
        description: "Session identifier for the chat"
      answer:
        type: "string"
        example: "The answer for your query"
        description: "Chatbot response answer"
    description: "Chat response from the chatbot service"
  ChatRequest:
    type: "object"
    required:
    - "prompt"
    properties:
      prompt:
        type: "string"
        example: "Get my brands"
        description: "User prompt for the chatbot"
        minLength: 0
        maxLength: 1000
    description: "Chat request containing user prompt"
  FeatureToggleDto:
    type: "object"
    required:
    - "enabled"
    - "name"
    - "strategy"
    properties:
      id:
        type: "integer"
        format: "int32"
        example: 1
        description: "Feature toggle ID"
      name:
        type: "string"
        example: "new_dashboard"
        description: "Feature name"
      description:
        type: "string"
        example: "New dashboard layout"
        description: "Feature description"
      enabled:
        type: "boolean"
        example: true
        description: "Whether feature is enabled"
      strategy:
        type: "string"
        example: "all_users"
        description: "Strategy for applying feature"
        enum:
        - "all_users"
        - "role_based"
        - "whitelist"
        - "beta_users"
    description: "Feature toggle configuration"
  JsonOkResponseFeatureToggleDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/FeatureToggleDto"
  CreateFeatureToggleRequest:
    type: "object"
    required:
    - "enabled"
    - "name"
    - "strategy"
    properties:
      name:
        type: "string"
        example: "new_dashboard"
        description: "Feature name"
      description:
        type: "string"
        example: "New dashboard layout"
        description: "Feature description"
      enabled:
        type: "boolean"
        example: true
        description: "Whether feature is enabled"
      strategy:
        type: "string"
        example: "all_users"
        description: "Strategy for applying feature"
        enum:
        - "all_users"
        - "role_based"
        - "whitelist"
        - "beta_users"
    description: "Request to create a new feature toggle"
  JsonOkListResponseFeatureToggleDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/FeatureToggleDto"
  UpdateFeatureToggleRequest:
    type: "object"
    required:
    - "enabled"
    - "strategy"
    properties:
      description:
        type: "string"
        example: "Updated dashboard layout"
        description: "Feature description"
      enabled:
        type: "boolean"
        example: true
        description: "Whether feature is enabled"
      strategy:
        type: "string"
        example: "all_users"
        description: "Strategy for applying feature"
        enum:
        - "all_users"
        - "role_based"
        - "whitelist"
        - "beta_users"
    description: "Request to update an existing feature toggle"
  Conversation:
    type: "object"
    properties:
      id:
        type: "string"
      self:
        type: "string"
      provider:
        type: "string"
        enum:
        - "INSTAGRAM"
        - "INSTAGRAMBUSINESS"
        - "TWITTER"
        - "FACEBOOK"
        - "GMB"
        - "TIKTOKBUSINESS"
        - "YOUTUBE"
        - "LINKEDIN"
      status:
        type: "string"
        enum:
        - "PENDING"
        - "READ"
        - "RESOLVED"
      creationDate:
        type: "string"
        format: "date-time"
      lastUpdateTime:
        type: "string"
        format: "date-time"
      lastReadTime:
        type: "string"
        format: "date-time"
      participants:
        type: "array"
        items:
          $ref: "#/definitions/Participant"
      messages:
        type: "array"
        items:
          $ref: "#/definitions/Message"
  JsonOkListResponseConversation:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Conversation"
  Message:
    type: "object"
    properties:
      id:
        type: "string"
      from:
        type: "string"
      to:
        type: "string"
      text:
        type: "string"
      publicationDateTime:
        type: "string"
        format: "date-time"
      attachments:
        type: "array"
        items:
          type: "string"
      properties:
        type: "object"
        additionalProperties:
          type: "object"
      status:
        type: "string"
        enum:
        - "NEW"
        - "READ"
        - "DELETED"
  Participant:
    type: "object"
    properties:
      id:
        type: "string"
      name:
        type: "string"
      email:
        type: "string"
      imageProfileUrl:
        type: "string"
  NewMessageRequest:
    type: "object"
    required:
    - "provider"
    properties:
      provider:
        type: "string"
      conversationId:
        type: "string"
      recipient:
        type: "string"
      text:
        type: "string"
      attachment:
        type: "string"
  Authorizations:
    type: "object"
    properties:
      missingScopes:
        type: "array"
        description: "List of the scopes needed to make the action. If you already\
          \ have it, this list will be empty"
        items:
          type: "string"
      allowAccessToMessages:
        type: "boolean"
        description: "Boolean that says if you has access to post comments feature"
  JsonOkResponseAuthorizations:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/Authorizations"
  InboxNote:
    type: "object"
    required:
    - "contextBlogId"
    - "created"
    - "id"
    - "provider"
    - "userId"
    properties:
      id:
        type: "integer"
        format: "int32"
      contextBlogId:
        type: "integer"
        format: "int32"
      participantScreenName:
        type: "string"
      participantAccountId:
        type: "string"
      provider:
        type: "string"
      userId:
        type: "integer"
        format: "int32"
      userName:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      content:
        type: "string"
      updatedDate:
        $ref: "#/definitions/DateTimeInfo"
      updated:
        type: "boolean"
      deletedDate:
        $ref: "#/definitions/DateTimeInfo"
      deleted:
        type: "boolean"
  JsonOkResponseInboxNote:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/InboxNote"
  InboxNoteRequest:
    type: "object"
    properties:
      participantScreenName:
        type: "string"
      participantAccountId:
        type: "string"
      provider:
        type: "string"
      content:
        type: "string"
  JsonOkListResponseInboxNote:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/InboxNote"
  ChangeStatusRequest:
    type: "object"
    required:
    - "conversationType"
    - "provider"
    properties:
      provider:
        type: "string"
      conversationType:
        type: "string"
      conversationId:
        type: "string"
      status:
        type: "string"
  Comment:
    type: "object"
    properties:
      parentId:
        type: "string"
      id:
        type: "string"
      creationDate:
        type: "string"
        format: "date-time"
      owner:
        type: "string"
      text:
        type: "string"
      mediaUrl:
        type: "string"
      properties:
        type: "object"
        additionalProperties:
          type: "object"
  Element:
    type: "object"
    properties:
      id:
        type: "string"
      owner:
        $ref: "#/definitions/Participant"
      link:
        type: "string"
      text:
        type: "string"
      mediaUrls:
        type: "array"
        items:
          type: "string"
      commentCount:
        type: "integer"
        format: "int32"
      reactionCount:
        type: "integer"
        format: "int32"
      properties:
        type: "object"
        additionalProperties:
          type: "object"
  JsonOkListResponsePostCommentsThread:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/PostCommentsThread"
  PostCommentsThread:
    type: "object"
    properties:
      id:
        type: "string"
      self:
        type: "string"
      provider:
        type: "string"
        enum:
        - "INSTAGRAM"
        - "INSTAGRAMBUSINESS"
        - "TWITTER"
        - "FACEBOOK"
        - "GMB"
        - "TIKTOKBUSINESS"
        - "YOUTUBE"
        - "LINKEDIN"
      status:
        type: "string"
        enum:
        - "PENDING"
        - "READ"
        - "RESOLVED"
      creationDate:
        type: "string"
        format: "date-time"
      lastUpdateTime:
        type: "string"
        format: "date-time"
      lastReadTime:
        type: "string"
        format: "date-time"
      participants:
        type: "array"
        items:
          $ref: "#/definitions/Participant"
      root:
        $ref: "#/definitions/RootComment"
  RootComment:
    type: "object"
    properties:
      element:
        $ref: "#/definitions/Element"
      id:
        type: "string"
      creationDate:
        type: "string"
        format: "date-time"
      owner:
        type: "string"
      text:
        type: "string"
      mediaUrl:
        type: "string"
      properties:
        type: "object"
        additionalProperties:
          type: "object"
      comments:
        type: "array"
        items:
          $ref: "#/definitions/Comment"
  NewCommentRequest:
    type: "object"
    required:
    - "provider"
    properties:
      provider:
        type: "string"
      objectId:
        type: "string"
      text:
        type: "string"
      attachment:
        type: "string"
  NewReplyRequest:
    type: "object"
    required:
    - "provider"
    properties:
      provider:
        type: "string"
      reviewId:
        type: "string"
      text:
        type: "string"
      attachment:
        type: "string"
  DeleteReplyRequest:
    type: "object"
    required:
    - "provider"
    properties:
      provider:
        type: "string"
      reviewId:
        type: "string"
  BusinessLocation:
    type: "object"
    properties:
      id:
        type: "string"
      url:
        type: "string"
      description:
        type: "string"
      properties:
        type: "object"
        additionalProperties:
          type: "object"
  JsonOkListResponseReview:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Review"
  Reply:
    type: "object"
    properties:
      comment:
        type: "string"
      updateTime:
        type: "string"
        format: "date-time"
  Review:
    type: "object"
    properties:
      id:
        type: "string"
      providerId:
        type: "string"
      self:
        type: "string"
      provider:
        type: "string"
        enum:
        - "INSTAGRAM"
        - "INSTAGRAMBUSINESS"
        - "TWITTER"
        - "FACEBOOK"
        - "GMB"
        - "TIKTOKBUSINESS"
        - "YOUTUBE"
        - "LINKEDIN"
      status:
        type: "string"
        enum:
        - "PENDING"
        - "READ"
        - "RESOLVED"
      creationDate:
        type: "string"
        format: "date-time"
      lastUpdateTime:
        type: "string"
        format: "date-time"
      lastReadTime:
        type: "string"
        format: "date-time"
      participants:
        type: "array"
        items:
          $ref: "#/definitions/Participant"
      message:
        type: "string"
      stars:
        type: "integer"
        format: "int32"
      reply:
        $ref: "#/definitions/Reply"
      element:
        $ref: "#/definitions/BusinessLocation"
  JsonOkListResponseLanguageInfo:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/LanguageInfo"
  LanguageInfo:
    type: "object"
    required:
    - "language"
    - "locale"
    properties:
      locale:
        type: "string"
      language:
        type: "string"
  JsonOkResponseSocialMediaSystemPromptResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/SocialMediaSystemPromptResponse"
  SocialMediaSystemPromptResponse:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      prompts:
        type: "object"
        additionalProperties:
          type: "string"
  JsonOkResponseSystemPromptResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/SystemPromptResponse"
  SystemPromptResponse:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      type:
        type: "string"
      prompt:
        type: "string"
  SocialMediaSystemPromptRequest:
    type: "object"
    properties:
      promptType:
        type: "string"
      promptText:
        type: "string"
  AssistantMessageResponse:
    type: "object"
    properties:
      threadId:
        type: "string"
      content:
        type: "string"
      contentList:
        type: "array"
        items:
          type: "string"
      spentCredits:
        type: "number"
        format: "double"
      userPrompt:
        type: "string"
  JsonOkResponseAssistantMessageResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/AssistantMessageResponse"
  AssistantMessageRequest:
    type: "object"
    properties:
      prompt:
        type: "string"
      imageUrl:
        type: "boolean"
      tone:
        type: "string"
      language:
        type: "string"
      network:
        type: "string"
      instructions:
        type: "string"
  VariantMessageRequest:
    type: "object"
    properties:
      userPost:
        type: "string"
      lastPost:
        type: "string"
      extraInstructions:
        type: "string"
  BlogLibraryPostDto:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      blogName:
        type: "string"
      blogPicture:
        type: "string"
      scheduledPostDate:
        $ref: "#/definitions/DateTimeInfo"
      libraryPost:
        $ref: "#/definitions/LibraryPostDto"
  BlueskyConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      postLanguages:
        type: "array"
        items:
          type: "string"
  FacebookConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      boostBudget:
        type: "number"
      boostPayer:
        type: "string"
      boostBeneficiary:
        type: "string"
      location:
        $ref: "#/definitions/LibraryPostLocationDto"
      type:
        type: "string"
      reelTitle:
        type: "string"
  GbpConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      type:
        type: "string"
  InstagramCollaboratorTag:
    type: "object"
    properties:
      username:
        type: "string"
      deleted:
        type: "boolean"
  InstagramConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      carouselTags:
        type: "object"
        additionalProperties:
          type: "array"
          items:
            $ref: "#/definitions/LibraryPostPeopleTagDto"
      carouselProductTags:
        type: "object"
        additionalProperties:
          type: "array"
          items:
            $ref: "#/definitions/LibraryPostProductTagDto"
      type:
        type: "string"
      showReelOnFeed:
        type: "boolean"
      boostBudget:
        type: "number"
      boostPayer:
        type: "string"
      boostBeneficiary:
        type: "string"
      location:
        $ref: "#/definitions/LibraryPostLocationDto"
      reelAudioName:
        type: "string"
      collaborators:
        type: "array"
        uniqueItems: true
        items:
          $ref: "#/definitions/InstagramCollaboratorTag"
  JobInfoResponse:
    type: "object"
    properties:
      jobId:
        type: "string"
      status:
        type: "string"
      blogId:
        type: "integer"
        format: "int32"
      scheduledStatus:
        type: "string"
      userInstructions:
        type: "string"
      createdDate:
        $ref: "#/definitions/DateTimeInfo"
      finishedDate:
        $ref: "#/definitions/DateTimeInfo"
      libraryPostId:
        type: "integer"
        format: "int64"
      result:
        type: "array"
        items:
          $ref: "#/definitions/BlogLibraryPostDto"
      postsCount:
        type: "integer"
        format: "int32"
      errorMessage:
        type: "string"
  JsonOkResponseJobInfoResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/JobInfoResponse"
  LibraryPostCommonConfigurationDto:
    type: "object"
    required:
    - "content"
    properties:
      content:
        type: "string"
      firstCommentText:
        type: "string"
      publishMode:
        type: "string"
      smartlinkData:
        $ref: "#/definitions/SmartlinkData"
  LibraryPostDto:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      creationDate:
        $ref: "#/definitions/DateTimeInfo"
      shortener:
        type: "boolean"
      draft:
        type: "boolean"
      commonData:
        $ref: "#/definitions/LibraryPostCommonConfigurationDto"
      media:
        type: "array"
        items:
          $ref: "#/definitions/LibraryPostMediaDto"
      saveExternalMediaFiles:
        type: "boolean"
      parentId:
        type: "integer"
        format: "int64"
      twitterData:
        $ref: "#/definitions/TwitterConfigurationDto"
      facebookData:
        $ref: "#/definitions/FacebookConfigurationDto"
      instagramData:
        $ref: "#/definitions/InstagramConfigurationDto"
      threadsData:
        $ref: "#/definitions/ThreadsConfigurationDto"
      linkedinData:
        $ref: "#/definitions/LinkedinConfigurationDto"
      pinterestData:
        $ref: "#/definitions/PinterestConfigurationDto"
      tiktokData:
        $ref: "#/definitions/TikTokConfigurationDto"
      youtubeData:
        $ref: "#/definitions/YoutubeConfigurationDto"
      gbpData:
        $ref: "#/definitions/GbpConfigurationDto"
      blueskyData:
        $ref: "#/definitions/BlueskyConfigurationDto"
      descendants:
        type: "array"
        items:
          $ref: "#/definitions/LibraryPostDto"
      notes:
        type: "array"
        items:
          $ref: "#/definitions/LibraryPostNoteDto"
      hasNotReadNotes:
        type: "boolean"
      tags:
        type: "string"
  LibraryPostLocationCoordinates:
    type: "object"
    properties:
      city:
        type: "string"
      country:
        type: "string"
      state:
        type: "string"
      street:
        type: "string"
      zip:
        type: "string"
      latitude:
        type: "number"
        format: "double"
      longitude:
        type: "number"
        format: "double"
  LibraryPostLocationDto:
    type: "object"
    properties:
      name:
        type: "string"
      link:
        type: "string"
      id:
        type: "string"
      locationCoordinates:
        $ref: "#/definitions/LibraryPostLocationCoordinates"
  LibraryPostMediaDto:
    type: "object"
    required:
    - "position"
    properties:
      id:
        type: "integer"
        format: "int64"
      position:
        type: "integer"
        format: "int32"
      url:
        type: "string"
      altText:
        type: "string"
      videoCoverMilliseconds:
        type: "integer"
        format: "int32"
      videoThumbnailUrl:
        type: "string"
  LibraryPostNoteDto:
    type: "object"
    required:
    - "created"
    - "id"
    - "libraryPostId"
    properties:
      id:
        type: "integer"
        format: "int64"
      libraryPostId:
        type: "integer"
        format: "int64"
      userId:
        type: "integer"
        format: "int32"
      agencyId:
        type: "integer"
        format: "int32"
      agencyUserId:
        type: "integer"
        format: "int32"
      userName:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      content:
        type: "string"
      updatedDate:
        $ref: "#/definitions/DateTimeInfo"
      updated:
        type: "boolean"
      deleted:
        type: "boolean"
  LibraryPostPeopleTagDto:
    type: "object"
    properties:
      username:
        type: "string"
      x:
        type: "number"
        format: "double"
      y:
        type: "number"
        format: "double"
  LibraryPostProductTagDto:
    type: "object"
    properties:
      productName:
        type: "string"
      productId:
        type: "string"
      x:
        type: "number"
        format: "double"
      y:
        type: "number"
        format: "double"
      catalogId:
        type: "string"
      position:
        type: "integer"
        format: "int32"
  LinkedinConfigurationDto:
    type: "object"
    required:
    - "previewIncluded"
    - "publishImagesAsPDF"
    properties:
      enabled:
        type: "boolean"
      documentTitle:
        type: "string"
      publishImagesAsPDF:
        type: "boolean"
      previewIncluded:
        type: "boolean"
      type:
        type: "string"
      poll:
        $ref: "#/definitions/LinkedinPollDto"
  LinkedinOptionDto:
    type: "object"
    properties:
      text:
        type: "string"
  LinkedinPollDto:
    type: "object"
    properties:
      question:
        type: "string"
      options:
        type: "array"
        items:
          $ref: "#/definitions/LinkedinOptionDto"
      settings:
        $ref: "#/definitions/LinkedinSettingsDto"
  LinkedinSettingsDto:
    type: "object"
    properties:
      duration:
        type: "string"
  PinterestConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      boardId:
        type: "string"
      pinTitle:
        type: "string"
      pinLink:
        type: "string"
      pinNewFormat:
        type: "boolean"
  ScheduledPostTwitterPoll:
    type: "object"
    properties:
      options:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostTwitterPollOption"
      settings:
        $ref: "#/definitions/ScheduledPostTwitterPollSettings"
  ScheduledPostTwitterPollOption:
    type: "object"
    properties:
      text:
        type: "string"
  ScheduledPostTwitterPollSettings:
    type: "object"
    properties:
      durationMinutes:
        type: "integer"
        format: "int32"
  SmartlinkData:
    type: "object"
    properties:
      targetUrl:
        type: "string"
      ids:
        type: "array"
        items:
          type: "integer"
          format: "int32"
  ThreadsConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      allowedCountryCodes:
        type: "array"
        uniqueItems: true
        items:
          type: "string"
      replyControl:
        type: "string"
  TikTokConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      disableComment:
        type: "boolean"
      disableDuet:
        type: "boolean"
      disableStitch:
        type: "boolean"
      privacyOption:
        type: "string"
      commercialContentThirdParty:
        type: "boolean"
      commercialContentOwnBrand:
        type: "boolean"
      title:
        type: "string"
      autoAddMusic:
        type: "boolean"
      photoCoverIndex:
        type: "integer"
        format: "int32"
      music:
        $ref: "#/definitions/TikTokTrackDto"
  TikTokTrackDto:
    type: "object"
    properties:
      musicId:
        type: "string"
      title:
        type: "string"
      author:
        type: "string"
      startMillis:
        type: "integer"
        format: "int64"
      durationMillis:
        type: "integer"
        format: "int64"
      startVideoMillis:
        type: "integer"
        format: "int64"
  TwitterConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      tags:
        type: "array"
        uniqueItems: true
        items:
          type: "string"
      replySettings:
        type: "string"
      type:
        type: "string"
      poll:
        $ref: "#/definitions/ScheduledPostTwitterPoll"
  YoutubeConfigurationDto:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      title:
        type: "string"
      type:
        type: "string"
      privacy:
        type: "string"
      tags:
        type: "array"
        uniqueItems: true
        items:
          type: "string"
      category:
        type: "string"
      madeForKids:
        type: "boolean"
      playlistId:
        type: "string"
  JobInfoRequest:
    type: "object"
    properties:
      userInstructions:
        type: "string"
      postData:
        $ref: "#/definitions/LibraryPostDto"
  UpdateJobStatusRequest:
    type: "object"
    properties:
      fieldName:
        type: "string"
  JsonOkListResponseJobInfoResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/JobInfoResponse"
  AiScheduledPost:
    type: "object"
    required:
    - "providers"
    - "publicationDate"
    properties:
      id:
        type: "integer"
        format: "int32"
      publicationDate:
        $ref: "#/definitions/DateTimeInfo"
      providers:
        type: "array"
        items:
          $ref: "#/definitions/ProviderStatus"
      descendants:
        type: "array"
        items:
          $ref: "#/definitions/AiScheduledPost"
      uuid:
        type: "string"
  JsonOkResponseNaturalLanguageScheduledPostsResultDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/NaturalLanguageScheduledPostsResultDto"
  NaturalLanguageScheduledPostsDto:
    type: "object"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      blogName:
        type: "string"
      blogPicture:
        type: "string"
      deleted:
        type: "boolean"
      post:
        $ref: "#/definitions/AiScheduledPost"
  NaturalLanguageScheduledPostsResultDto:
    type: "object"
    properties:
      userInstructions:
        type: "string"
        description: "Instructions introduced by the user for scheduling posts with\
          \ AI"
      posts:
        type: "array"
        description: "List of natural language scheduled posts"
        items:
          $ref: "#/definitions/NaturalLanguageScheduledPostsDto"
    description: "Full info of natural language scheduled posts"
  ProviderStatus:
    type: "object"
    properties:
      network:
        type: "string"
      id:
        type: "string"
      status:
        type: "string"
        enum:
        - "PUBLISHED"
        - "PUBLISHING"
        - "PENDING"
        - "ERROR"
        - "DRAFT"
      publicUrl:
        type: "string"
      detailedStatus:
        type: "string"
  CanvaAssetSummary:
    type: "object"
    properties:
      type:
        type: "string"
      id:
        type: "string"
      name:
        type: "string"
      tags:
        type: "array"
        items:
          type: "string"
      created_at:
        type: "integer"
        format: "int32"
      updated_at:
        type: "integer"
        format: "int32"
      thumbnail:
        $ref: "#/definitions/CanvaThumbnail"
  CanvaDesign:
    type: "object"
    properties:
      id:
        type: "string"
      urls:
        $ref: "#/definitions/CanvaDesignLinks"
      created_at:
        type: "integer"
        format: "int32"
      updated_at:
        type: "integer"
        format: "int32"
      title:
        type: "string"
      thumbnail:
        $ref: "#/definitions/CanvaThumbnail"
      page_count:
        type: "integer"
        format: "int32"
  CanvaDesignLinks:
    type: "object"
    properties:
      edit_url:
        type: "string"
      view_url:
        type: "string"
  CanvaFolder:
    type: "object"
    properties:
      id:
        type: "string"
      name:
        type: "string"
      created_at:
        type: "integer"
        format: "int32"
      updated_at:
        type: "integer"
        format: "int32"
      thumbnail:
        $ref: "#/definitions/CanvaThumbnail"
  CanvaFolderContent:
    type: "object"
    properties:
      items:
        type: "array"
        items:
          $ref: "#/definitions/CanvaFolderItemSummary"
      continuation:
        type: "string"
  CanvaFolderItemSummary:
    type: "object"
    properties:
      type:
        type: "string"
      folder:
        $ref: "#/definitions/CanvaFolder"
      design:
        $ref: "#/definitions/CanvaDesign"
      image:
        $ref: "#/definitions/CanvaAssetSummary"
      template:
        $ref: "#/definitions/CanvaTemplate"
  CanvaTemplate:
    type: "object"
    properties:
      id:
        type: "string"
      title:
        type: "string"
      url:
        type: "string"
      thumbnails:
        type: "array"
        items:
          $ref: "#/definitions/CanvaThumbnail"
  CanvaThumbnail:
    type: "object"
    properties:
      width:
        type: "integer"
        format: "int32"
      height:
        type: "integer"
        format: "int32"
      url:
        type: "string"
  CanvaUserDesigns:
    type: "object"
    properties:
      continuation:
        type: "string"
      items:
        type: "array"
        items:
          $ref: "#/definitions/CanvaDesign"
  CanvaExportError:
    type: "object"
    properties:
      code:
        type: "string"
      message:
        type: "string"
  CanvaExportJob:
    type: "object"
    properties:
      job:
        $ref: "#/definitions/CanvaJob"
  CanvaJob:
    type: "object"
    properties:
      id:
        type: "string"
      status:
        type: "string"
      urls:
        type: "array"
        items:
          type: "string"
      error:
        $ref: "#/definitions/CanvaExportError"
  CanvaExportFormat:
    type: "object"
    properties:
      type:
        type: "string"
      quality:
        type: "string"
      pages:
        type: "array"
        items:
          type: "integer"
          format: "int32"
      export_quality:
        type: "string"
      width:
        type: "integer"
        format: "int32"
      height:
        type: "integer"
        format: "int32"
      lossless:
        type: "boolean"
      as_single_image:
        type: "boolean"
      size:
        type: "string"
  CanvaExportRequest:
    type: "object"
    properties:
      design_id:
        type: "string"
      format:
        $ref: "#/definitions/CanvaExportFormat"
  CanvaUserProfile:
    type: "object"
    properties:
      profile:
        $ref: "#/definitions/CanvaUserProfileProperties"
  CanvaUserProfileProperties:
    type: "object"
    properties:
      display_name:
        type: "string"
  CanvaTeamUserSummary:
    type: "object"
    properties:
      user_id:
        type: "string"
      team_id:
        type: "string"
  CanvaUserDetails:
    type: "object"
    properties:
      team_user:
        $ref: "#/definitions/CanvaTeamUserSummary"
  DriveFileResponse:
    type: "object"
    properties:
      createdTime:
        type: "string"
      iconLink:
        type: "string"
      id:
        type: "string"
      kind:
        type: "string"
      mimeType:
        type: "string"
      name:
        type: "string"
      size:
        type: "string"
      modifiedTime:
        type: "string"
      ownedByMe:
        type: "boolean"
      owners:
        type: "array"
        items:
          $ref: "#/definitions/DriveUserDetailsResponse"
      parents:
        type: "array"
        items:
          type: "string"
      permissions:
        type: "array"
        items:
          $ref: "#/definitions/DrivePermissionsResponse"
      shared:
        type: "boolean"
      webViewLink:
        type: "string"
      webContentLink:
        type: "string"
      thumbnailLink:
        type: "string"
      imageMediaMetadata:
        $ref: "#/definitions/ImageMediaMetadataResponse"
      videoMediaMetadata:
        $ref: "#/definitions/VideoMediaMetadataResponse"
  DrivePermissionsResponse:
    type: "object"
    properties:
      deleted:
        type: "boolean"
      displayName:
        type: "string"
      emailAddress:
        type: "string"
      id:
        type: "string"
      kind:
        type: "string"
      photoLink:
        type: "string"
      role:
        type: "string"
      type:
        type: "string"
  DriveUserDetailsResponse:
    type: "object"
    properties:
      displayName:
        type: "string"
      emailAddress:
        type: "string"
      kind:
        type: "string"
      me:
        type: "boolean"
      permissionId:
        type: "string"
      photoLink:
        type: "string"
  ImageMediaMetadataResponse:
    type: "object"
    properties:
      rotation:
        type: "integer"
        format: "int32"
      height:
        type: "integer"
        format: "int32"
      width:
        type: "integer"
        format: "int32"
  VideoMediaMetadataResponse:
    type: "object"
    properties:
      durationMillis:
        type: "string"
      height:
        type: "integer"
        format: "int32"
      width:
        type: "integer"
        format: "int32"
  DriveResponse:
    type: "object"
    properties:
      id:
        type: "string"
      name:
        type: "string"
  DriveDrivesRequest:
    type: "object"
    properties:
      pageSize:
        type: "integer"
        format: "int32"
      pageToken:
        type: "string"
      q:
        type: "string"
      useDomainAdminAccess:
        type: "boolean"
  DriveFileListResponse:
    type: "object"
    properties:
      nextPageToken:
        type: "string"
      files:
        type: "array"
        items:
          $ref: "#/definitions/DriveFileResponse"
  DriveFilesRequest:
    type: "object"
    properties:
      orderBy:
        type: "string"
      pageToken:
        type: "string"
      pageSize:
        type: "integer"
        format: "int32"
      q:
        type: "string"
      includeItemsFromAllDrives:
        type: "boolean"
      supportsAllDrives:
        type: "boolean"
  CustomizedUserConfiguration:
    type: "object"
    properties:
      embeddedUrl:
        type: "string"
  JsonOkResponseReportConfiguration:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/ReportConfiguration"
  ReportConfiguration:
    type: "object"
    required:
    - "blogId"
    - "userId"
    properties:
      blogId:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      reportType:
        type: "string"
      reportLogo:
        type: "string"
      emails:
        type: "array"
        items:
          type: "string"
      automaticReportDate:
        type: "integer"
        format: "int32"
      text:
        type: "string"
      subscribe:
        type: "boolean"
      saveMonthlySetup:
        type: "boolean"
      reportParameters:
        $ref: "#/definitions/ReportParameters"
  ReportParameters:
    type: "object"
    properties:
      enabledCheckbox:
        type: "array"
        items:
          type: "string"
      sections:
        type: "object"
        additionalProperties:
          $ref: "#/definitions/SocialMediaParams"
      language:
        type: "string"
      templateId:
        type: "string"
  SocialMediaParams:
    type: "object"
    properties:
      rankingField:
        type: "string"
      postsCount:
        type: "integer"
        format: "int32"
  MailDemoReport:
    type: "object"
    properties:
      email:
        type: "string"
      subject:
        type: "string"
      text:
        type: "string"
  JsonOkResponseReportStatusInfo:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/ReportStatusInfo"
  ReportStatusInfo:
    type: "object"
    properties:
      status:
        type: "string"
      reportPath:
        type: "string"
  ReportRequest:
    type: "object"
  JsonOkListResponseReportHistoryItem:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ReportHistoryItem"
  ReportHistoryItem:
    type: "object"
    properties:
      creationDate:
        type: "string"
        format: "date-time"
      from:
        type: "string"
      to:
        type: "string"
      rss:
        type: "boolean"
      twitter:
        type: "boolean"
      facebook:
        type: "boolean"
      facebookAds:
        type: "boolean"
      instagram:
        type: "boolean"
      threads:
        type: "boolean"
      bluesky:
        type: "boolean"
      linkedin:
        type: "boolean"
      pinterest:
        type: "boolean"
      tiktok:
        type: "boolean"
      adwords:
        type: "boolean"
      gmb:
        type: "boolean"
      youtube:
        type: "boolean"
      twitch:
        type: "boolean"
      tiktokAds:
        type: "boolean"
      brandSummary:
        type: "boolean"
      reportType:
        type: "string"
      reportFile:
        type: "string"
      status:
        type: "string"
        enum:
        - "PENDING"
        - "RUNNING"
        - "RETRYING"
        - "FINISHED"
        - "FAILED"
      engineVersion:
        type: "string"
  ApprovalTask:
    type: "object"
    properties:
      publicationDate:
        $ref: "#/definitions/DateTimeInfo"
      postId:
        type: "integer"
        format: "int32"
      postUuid:
        type: "string"
      mediaUrl:
        type: "string"
      text:
        type: "string"
      networks:
        type: "array"
        items:
          type: "string"
      status:
        type: "string"
      blogId:
        type: "integer"
        format: "int32"
      blogName:
        type: "string"
      taskType:
        type: "string"
      approvalTaskUsers:
        type: "array"
        items:
          $ref: "#/definitions/ApprovalTaskUser"
  ApprovalTaskUser:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      mail:
        type: "string"
      fullName:
        type: "string"
      status:
        type: "string"
  JsonOkListResponseApprovalTask:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ApprovalTask"
  JsonOkResponseInteger:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "integer"
        format: "int32"
  JsonOkResponseOpenedTasksCount:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/OpenedTasksCount"
  OpenedTasksCount:
    type: "object"
    properties:
      total:
        type: "integer"
        format: "int32"
      details:
        type: "array"
        items:
          $ref: "#/definitions/TasksCountDetails"
  TasksCountDetails:
    type: "object"
  BestTimes:
    type: "object"
    properties:
      dayOfWeek:
        type: "integer"
        format: "int32"
      bestTimesByHour:
        type: "array"
        items:
          $ref: "#/definitions/BestTimesByHour"
  BestTimesByHour:
    type: "object"
    properties:
      hourOfDay:
        type: "integer"
        format: "int32"
      value:
        type: "integer"
        format: "int32"
  JsonOkListResponseBestTimes:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BestTimes"
  Board:
    type: "object"
    required:
    - "name"
    properties:
      id:
        type: "string"
      name:
        type: "string"
      description:
        type: "string"
      owner:
        $ref: "#/definitions/BoardOwner"
      privacy:
        type: "string"
  BoardOwner:
    type: "object"
    properties:
      username:
        type: "string"
  JsonOkListResponseBoard:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Board"
  JsonOkResponseBoard:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/Board"
  IGCatalog:
    type: "object"
    properties:
      catalogId:
        type: "string"
      catalogName:
        type: "string"
      shopName:
        type: "string"
      productCount:
        type: "integer"
        format: "int32"
  JsonOkListResponseIGCatalog:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/IGCatalog"
  IGCatalogProduct:
    type: "object"
    properties:
      productId:
        type: "string"
      merchantId:
        type: "string"
      productName:
        type: "string"
      imageUrl:
        type: "string"
      retailerId:
        type: "string"
      reviewStatus:
        type: "string"
      isCheckoutFlow:
        type: "boolean"
      productVariants:
        type: "array"
        items:
          $ref: "#/definitions/ProductVariant"
  JsonOkListResponseIGCatalogProduct:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/IGCatalogProduct"
  ProductVariant:
    type: "object"
    properties:
      productId:
        type: "string"
      variantName:
        type: "string"
  JsonOkResponseListYoutubeVideoCategory:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/YoutubeVideoCategory"
  YoutubeVideoCategory:
    type: "object"
    properties:
      key:
        type: "string"
      label:
        type: "string"
  JsonOkResponseListYoutubePlaylistDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/YoutubePlaylistDto"
  YoutubePlaylistDto:
    type: "object"
    properties:
      id:
        type: "string"
        example: "PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG"
        description: "Unique identifier of the playlist"
      title:
        type: "string"
        example: "My channel uploads"
        description: "Playlist title (human readable)"
    description: "Represents a YouTube playlist linked to a channel. Contains the\
      \ playlist id and its human readable title."
  FacebookRecommendedAudio:
    type: "object"
    properties:
      title:
        type: "string"
      artist:
        type: "string"
      displayImageUri:
        type: "string"
  JsonOkListResponseFacebookRecommendedAudio:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/FacebookRecommendedAudio"
  JsonOkResponseTikTokCreatorInfo:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/TikTokCreatorInfo"
  TikTokCreatorInfo:
    type: "object"
    properties:
      creatorAvatarUrl:
        type: "string"
      creatorUsername:
        type: "string"
      creatorNickname:
        type: "string"
      privacyLevelOptions:
        type: "array"
        items:
          type: "string"
      commentDisabled:
        type: "boolean"
      duetDisabled:
        type: "boolean"
      stitchDisabled:
        type: "boolean"
      maxVideoPostDurationSec:
        type: "integer"
        format: "int32"
  JsonOkListResponseTikTokTrendingTrackDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/TikTokTrendingTrackDto"
  TikTokTrendingTrackDto:
    type: "object"
    properties:
      commercialMusicId:
        type: "string"
      commercialMusicName:
        type: "string"
      duration:
        type: "integer"
        format: "int32"
      thumbnailUrl:
        type: "string"
      artist:
        type: "string"
      previewUrl:
        type: "string"
      genres:
        type: "array"
        items:
          type: "string"
      rankPosition:
        type: "string"
  JsonOkResponseSchedulerCounters:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/SchedulerCounters"
  SchedulerCounters:
    type: "object"
    properties:
      monthPublishedPostsByUser:
        type: "integer"
        format: "int64"
      monthPublishedPostsByBrand:
        type: "integer"
        format: "int64"
      last24HoursPublishedYoutubePostsByBrand:
        type: "integer"
        format: "int64"
      aiCopiesAttemptsUsedThisMonth:
        type: "integer"
        format: "int64"
      aiSpentCreditsThisMonth:
        type: "number"
        format: "double"
  CalendarDto:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      url:
        type: "string"
      name:
        type: "string"
      description:
        type: "string"
      publicCalendar:
        type: "boolean"
      timeZone:
        type: "string"
      language:
        type: "string"
      type:
        type: "string"
        enum:
        - "SYSTEM"
        - "USER"
      events:
        type: "array"
        items:
          $ref: "#/definitions/EventDto"
  DailyFrecuency:
    type: "object"
    properties:
      dayOfWeek:
        type: "string"
        enum:
        - "MONDAY"
        - "TUESDAY"
        - "WEDNESDAY"
        - "THURSDAY"
        - "FRIDAY"
        - "SATURDAY"
        - "SUNDAY"
      position:
        type: "integer"
        format: "int32"
  EventDto:
    type: "object"
    properties:
      name:
        type: "string"
      description:
        type: "string"
      eventInit:
        type: "string"
        format: "date-time"
      eventEnd:
        type: "string"
        format: "date-time"
      repeatEvent:
        type: "boolean"
      repeat:
        $ref: "#/definitions/RepeatFrequencyDto"
      dailyEvent:
        type: "boolean"
      uid:
        type: "string"
  JsonOkResponseCalendarDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/CalendarDto"
  RepeatFrequencyDto:
    type: "object"
    properties:
      repeatPattern:
        type: "string"
      frequency:
        type: "string"
        enum:
        - "NANOS"
        - "MICROS"
        - "MILLIS"
        - "SECONDS"
        - "MINUTES"
        - "HOURS"
        - "HALF_DAYS"
        - "DAYS"
        - "WEEKS"
        - "MONTHS"
        - "YEARS"
        - "DECADES"
        - "CENTURIES"
        - "MILLENNIA"
        - "ERAS"
        - "FOREVER"
      daysOfWeek:
        type: "array"
        items:
          $ref: "#/definitions/DailyFrecuency"
      daysOfMoth:
        type: "array"
        items:
          type: "integer"
          format: "int32"
      interval:
        type: "integer"
        format: "int32"
      repeatCount:
        type: "integer"
        format: "int32"
      until:
        type: "string"
        format: "date-time"
  JsonOkResponseResult Information About Added Calendar To A User Or Blog:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/result information about added calendar to a user or\
          \ blog"
  result information about added calendar to a user or blog:
    type: "object"
    required:
    - "calendarId"
    properties:
      calendarId:
        type: "integer"
        format: "int32"
        description: "Internal calendar id"
      aggregationTo:
        type: "integer"
        format: "int32"
        description: "Blog id, if it is add for a blog"
      userId:
        type: "integer"
        format: "int32"
        description: "User id, if it is add for a user"
  Information about adding a calendar to an user or blog:
    type: "object"
    required:
    - "aggregationFrom"
    properties:
      aggregationFrom:
        type: "string"
        description: "Adding for a user or blog"
  ICS calendar response data:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
        example: 1234
        description: "Internal calendar Id"
      url:
        type: "string"
        example: "https://calendar.google.com/calendar/ical/c_very long number.group.calendar.google.com/public/basic.ics"
        description: "external url to access a public ICS file with this calendar\
          \ information"
      name:
        type: "string"
        example: "calendar"
        description: "Calendar name"
      description:
        type: "string"
        example: "Description text"
        description: "Calendar description"
      publicCalendar:
        type: "boolean"
        example: false
        description: "Is this calendar visible to user?"
      language:
        type: "string"
        description: "Calendar language"
      type:
        type: "string"
        example: "system"
        description: "Calendar type"
        enum:
        - "system"
        - "user"
  JsonOkListResponseICS Calendar Response Data:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ICS calendar response data"
  JsonOkResponseTwo List With CalendarDTO, User's Calendars And Blog's Calendars:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/two list with CalendarDTO, user's calendars and blog's\
          \ calendars"
  two list with CalendarDTO, user's calendars and blog's calendars:
    type: "object"
    properties:
      userCalendars:
        type: "array"
        description: "Calendars assigned to current user"
        items:
          $ref: "#/definitions/ICS calendar response data"
      blogCalendars:
        type: "array"
        description: "Calendars assigned to current blog"
        items:
          $ref: "#/definitions/ICS calendar response data"
  Response about remove a calendar for an user or blog:
    type: "object"
    required:
    - "removeFrom"
    properties:
      removeFrom:
        type: "string"
        description: "Erase calendar for a user or blog"
  All events in limited time in one calendar:
    type: "object"
    properties:
      calendar-id:
        type: "integer"
        format: "int32"
        description: "Calendar id"
      calendar-name:
        type: "string"
        description: "Calendar name"
      start-date:
        description: "Start limited time"
        $ref: "#/definitions/DateTimeInfo"
      end-date:
        description: "End limited time"
        $ref: "#/definitions/DateTimeInfo"
      events-all-day:
        type: "array"
        description: "Events all day"
        items:
          $ref: "#/definitions/Atomic event, with init and end one time"
      events-by-hour:
        type: "array"
        description: "Events with init hour and end hour"
        items:
          $ref: "#/definitions/Atomic event, with init and end one time"
  Atomic event, with init and end one time:
    type: "object"
    properties:
      eventName:
        type: "string"
        description: "Event name"
      eventDescription:
        type: "string"
        description: "Event description"
      eventInit:
        description: "Event init time"
        $ref: "#/definitions/DateTimeInfo"
      eventEnd:
        description: "Event ent time"
        $ref: "#/definitions/DateTimeInfo"
      uid:
        type: "string"
  JsonOkResponseAll Events In Limited Time In One Calendar:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/All events in limited time in one calendar"
  JsonOkResponseICS Calendar Response Data:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/ICS calendar response data"
  ICS calendar request data:
    type: "object"
    required:
    - "aggregationFrom"
    properties:
      id:
        type: "integer"
        format: "int32"
        example: 1234
        description: "Internal calendar Id"
      url:
        type: "string"
        example: "https://calendar.google.com/calendar/ical/c_very long number.group.calendar.google.com/public/basic.ics"
        description: "external url to access a public ICS file with this calendar\
          \ information"
      name:
        type: "string"
        example: "calendar"
        description: "Calendar name"
      description:
        type: "string"
        example: "Description text"
        description: "Calendar description"
      publicCalendar:
        type: "boolean"
        example: false
        description: "Is this calendar visible to user?"
      language:
        type: "string"
        description: "Calendar language"
      aggregationFrom:
        type: "string"
        description: "Adding for a user or blog"
  JsonOkResponsePlannerNotificationConfiguration:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/PlannerNotificationConfiguration"
  PlannerNotificationConfiguration:
    type: "object"
    properties:
      notificationType:
        type: "string"
      emailList:
        type: "array"
        items:
          $ref: "#/definitions/UserMail"
      deviceList:
        type: "array"
        items:
          $ref: "#/definitions/UserDevice"
  UserDevice:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      userId:
        type: "integer"
        format: "int32"
      username:
        type: "string"
      model:
        type: "string"
      platform:
        type: "string"
      version:
        type: "string"
      manufacturer:
        type: "string"
      appVersion:
        type: "string"
      label:
        type: "string"
      update:
        $ref: "#/definitions/DateTimeInfo"
      status:
        type: "string"
  UserMail:
    type: "object"
    properties:
      userId:
        type: "integer"
        format: "int32"
      blogId:
        type: "integer"
        format: "int32"
      username:
        type: "string"
      mail:
        type: "string"
  PlannerNotificationConfigurationRequest:
    type: "object"
    required:
    - "deviceList"
    - "emailList"
    properties:
      notificationType:
        type: "string"
      emailList:
        type: "array"
        items:
          $ref: "#/definitions/UserMailRequest"
      deviceList:
        type: "array"
        items:
          $ref: "#/definitions/UserDeviceRequest"
      sendTest:
        type: "boolean"
  UserDeviceRequest:
    type: "object"
    required:
    - "id"
    - "userId"
    properties:
      id:
        type: "integer"
        format: "int64"
      userId:
        type: "integer"
        format: "int32"
      username:
        type: "string"
      status:
        type: "string"
  UserMailRequest:
    type: "object"
    required:
    - "blogId"
    - "userId"
    properties:
      userId:
        type: "integer"
        format: "int32"
      blogId:
        type: "integer"
        format: "int32"
      username:
        type: "string"
      mail:
        type: "string"
  ScheduledPostUpdateRequest:
    type: "object"
    required:
    - "publicationDate"
    properties:
      publicationDate:
        $ref: "#/definitions/DateTimeInfo"
  JsonOkListResponseScheduledPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPost"
  ScheduledPost:
    type: "object"
    required:
    - "providers"
    - "publicationDate"
    - "text"
    properties:
      id:
        type: "integer"
        format: "int32"
      publicationDate:
        $ref: "#/definitions/DateTimeInfo"
      creationDate:
        $ref: "#/definitions/DateTimeInfo"
      text:
        type: "string"
      firstCommentText:
        type: "string"
      providers:
        type: "array"
        items:
          $ref: "#/definitions/ProviderStatus"
      media:
        type: "array"
        items:
          type: "string"
      autoPublish:
        type: "boolean"
      saveExternalMediaFiles:
        type: "boolean"
      mediaAltText:
        type: "array"
        items:
          type: "string"
      shortener:
        type: "boolean"
      draft:
        type: "boolean"
      location:
        $ref: "#/definitions/ScheduledPostLocation"
      videoCoverMilliseconds:
        type: "integer"
        format: "int64"
      videoThumbnailUrl:
        type: "string"
      parentId:
        type: "integer"
        format: "int32"
      twitterData:
        $ref: "#/definitions/ScheduledPostTwitterData"
      facebookData:
        $ref: "#/definitions/ScheduledPostFacebookData"
      smartLinkData:
        $ref: "#/definitions/ScheduledPostSmartLinkData"
      instagramData:
        $ref: "#/definitions/ScheduledPostInstagramData"
      pinterestData:
        $ref: "#/definitions/ScheduledPostPinterestData"
      youtubeData:
        $ref: "#/definitions/ScheduledPostYoutubeData"
      tiktokData:
        $ref: "#/definitions/ScheduledPostTikTokData"
      linkedinData:
        $ref: "#/definitions/ScheduledPostLinkedinData"
      autolistData:
        $ref: "#/definitions/ScheduledPostAutolistData"
      brandName:
        type: "string"
      targetBrandId:
        type: "integer"
        format: "int32"
      gmbData:
        $ref: "#/definitions/ScheduledPostGmbData"
      descendants:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPost"
      notes:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostNote"
      hasNotReadNotes:
        type: "boolean"
      uuid:
        type: "string"
      copiedFrom:
        type: "string"
      creatorUserMail:
        type: "string"
      creatorUserId:
        type: "integer"
        format: "int32"
      creatorAgencyUserMail:
        type: "string"
      creatorAgencyId:
        type: "integer"
        format: "int32"
      creatorAgencyUserId:
        type: "integer"
        format: "int32"
      postApprovalData:
        $ref: "#/definitions/ScheduledPostApprovalData"
      threadsData:
        $ref: "#/definitions/ScheduledPostThreadsData"
      blueskyData:
        $ref: "#/definitions/ScheduledPostBlueskyData"
      libraryPostId:
        type: "integer"
        format: "int64"
  ScheduledPostApprovalData:
    type: "object"
    required:
    - "approvalEvents"
    properties:
      approvalStatus:
        type: "string"
      approvalCriteria:
        type: "string"
      approvalEvents:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostApprovalEvent"
      sendMailToReviewers:
        type: "boolean"
      saveData:
        type: "boolean"
  ScheduledPostApprovalEvent:
    type: "object"
    properties:
      postUuid:
        type: "string"
      postId:
        type: "integer"
        format: "int32"
      reviewerId:
        type: "integer"
        format: "int32"
      reviewerMail:
        type: "string"
      status:
        type: "string"
      updatedDate:
        $ref: "#/definitions/DateTimeInfo"
      deletedDate:
        $ref: "#/definitions/DateTimeInfo"
      deleted:
        type: "boolean"
  ScheduledPostAutolistData:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      name:
        type: "string"
  ScheduledPostBlueskyData:
    type: "object"
    properties:
      postLanguages:
        type: "array"
        items:
          type: "string"
  ScheduledPostFacebookData:
    type: "object"
    properties:
      boost:
        type: "number"
        format: "double"
      boostPayer:
        type: "string"
      boostBeneficiary:
        type: "string"
      type:
        type: "string"
      title:
        type: "string"
  ScheduledPostGmbData:
    type: "object"
    properties:
      type:
        type: "string"
  ScheduledPostImageTag:
    type: "object"
    properties:
      username:
        type: "string"
      x:
        type: "number"
        format: "double"
      y:
        type: "number"
        format: "double"
      deleted:
        type: "boolean"
  ScheduledPostInstagramData:
    type: "object"
    properties:
      autoPublish:
        type: "boolean"
      tags:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostImageTag"
      productTags:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostProductTag"
      carouselTags:
        type: "object"
        additionalProperties:
          type: "array"
          items:
            $ref: "#/definitions/ScheduledPostImageTag"
      carouselProductTags:
        type: "object"
        additionalProperties:
          type: "array"
          items:
            $ref: "#/definitions/ScheduledPostProductTag"
      type:
        type: "string"
      showReelOnFeed:
        type: "boolean"
      boost:
        type: "number"
        format: "double"
      boostPayer:
        type: "string"
      boostBeneficiary:
        type: "string"
      audioName:
        type: "string"
      collaborators:
        type: "array"
        items:
          $ref: "#/definitions/InstagramCollaboratorTag"
  ScheduledPostLinkedinData:
    type: "object"
    properties:
      documentTitle:
        type: "string"
      publishImagesAsPDF:
        type: "boolean"
      previewIncluded:
        type: "boolean"
      type:
        type: "string"
      poll:
        $ref: "#/definitions/ScheduledPostLinkedinPoll"
  ScheduledPostLinkedinPoll:
    type: "object"
    properties:
      question:
        type: "string"
      options:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostLinkedinPollOption"
      settings:
        $ref: "#/definitions/ScheduledPostLinkedinPollSettings"
  ScheduledPostLinkedinPollOption:
    type: "object"
    properties:
      text:
        type: "string"
  ScheduledPostLinkedinPollSettings:
    type: "object"
    properties:
      duration:
        type: "string"
  ScheduledPostLocation:
    type: "object"
    properties:
      name:
        type: "string"
      link:
        type: "string"
      id:
        type: "string"
      location:
        $ref: "#/definitions/ScheduledPostLocationCoordinates"
      deleted:
        type: "boolean"
  ScheduledPostLocationCoordinates:
    type: "object"
    properties:
      city:
        type: "string"
      country:
        type: "string"
      state:
        type: "string"
      street:
        type: "string"
      zip:
        type: "string"
      latitude:
        type: "number"
        format: "double"
      longitude:
        type: "number"
        format: "double"
  ScheduledPostNote:
    type: "object"
    required:
    - "created"
    - "id"
    - "postId"
    properties:
      id:
        type: "integer"
        format: "int32"
      postId:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      agencyId:
        type: "integer"
        format: "int32"
      userName:
        type: "string"
      created:
        $ref: "#/definitions/DateTimeInfo"
      content:
        type: "string"
      updatedDate:
        $ref: "#/definitions/DateTimeInfo"
      updated:
        type: "boolean"
      deletedDate:
        $ref: "#/definitions/DateTimeInfo"
      deleted:
        type: "boolean"
  ScheduledPostPinterestData:
    type: "object"
    properties:
      boardId:
        type: "string"
      pinTitle:
        type: "string"
      pinLink:
        type: "string"
      pinNewFormat:
        type: "boolean"
  ScheduledPostProductTag:
    type: "object"
    properties:
      productName:
        type: "string"
      productId:
        type: "string"
      x:
        type: "number"
        format: "double"
      y:
        type: "number"
        format: "double"
      catalogId:
        type: "string"
  ScheduledPostSmartLinkData:
    type: "object"
    properties:
      targetUrl:
        type: "string"
      ids:
        type: "array"
        items:
          type: "integer"
          format: "int32"
  ScheduledPostThreadsData:
    type: "object"
    properties:
      allowedCountryCodes:
        type: "array"
        items:
          type: "string"
      replyControl:
        type: "string"
  ScheduledPostTikTokData:
    type: "object"
    properties:
      disableComment:
        type: "boolean"
      disableDuet:
        type: "boolean"
      disableStitch:
        type: "boolean"
      privacyOption:
        type: "string"
      commercialContentThirdParty:
        type: "boolean"
      commercialContentOwnBrand:
        type: "boolean"
      title:
        type: "string"
      autoAddMusic:
        type: "boolean"
      photoCoverIndex:
        type: "integer"
        format: "int32"
      music:
        $ref: "#/definitions/ScheduledPostTikTokTrack"
  ScheduledPostTikTokTrack:
    type: "object"
    properties:
      musicId:
        type: "string"
      title:
        type: "string"
      author:
        type: "string"
      startMillis:
        type: "integer"
        format: "int64"
      durationMillis:
        type: "integer"
        format: "int64"
      startVideoMillis:
        type: "integer"
        format: "int64"
  ScheduledPostTwitterData:
    type: "object"
    properties:
      tags:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostImageTag"
      replySettings:
        type: "string"
      type:
        type: "string"
      poll:
        $ref: "#/definitions/ScheduledPostTwitterPoll"
  ScheduledPostYoutubeData:
    type: "object"
    properties:
      title:
        type: "string"
      type:
        type: "string"
      privacy:
        type: "string"
      tags:
        type: "array"
        items:
          type: "string"
      category:
        type: "string"
      playlistId:
        type: "string"
      madeForKids:
        type: "boolean"
  JsonOkResponseScheduledPost:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/ScheduledPost"
  ScheduledPostApprovalEventRequest:
    type: "object"
    required:
    - "reviewerId"
    - "status"
    properties:
      postUuid:
        type: "string"
      reviewerId:
        type: "integer"
        format: "int32"
      status:
        type: "string"
      noteContent:
        type: "string"
  BrandPossibleSchedulerReviewer:
    type: "object"
    properties:
      userId:
        type: "integer"
        format: "int32"
      mail:
        type: "string"
      fullName:
        type: "string"
      selected:
        type: "boolean"
  BrandSchedulerPostApprovalData:
    type: "object"
    required:
    - "possibleReviewers"
    properties:
      approvalStatus:
        type: "string"
      approvalCriteria:
        type: "string"
      possibleReviewers:
        type: "array"
        items:
          $ref: "#/definitions/BrandPossibleSchedulerReviewer"
      sendMailToReviewers:
        type: "boolean"
  JsonOkResponseBrandSchedulerPostApprovalData:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/BrandSchedulerPostApprovalData"
  JsonOkListResponseScheduledPostApprovalDataUpdateResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostApprovalDataUpdateResponse"
  ScheduledPostApprovalDataUpdateResponse:
    type: "object"
    properties:
      uuid:
        type: "string"
      id:
        type: "integer"
        format: "int32"
      status:
        type: "string"
      detail:
        type: "object"
  ScheduledPostApprovalDataInBulk:
    type: "object"
    required:
    - "approvalData"
    - "posts"
    properties:
      approvalData:
        $ref: "#/definitions/ScheduledPostApprovalData"
      posts:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPost"
  InstagramAutoPublishProperties:
    type: "object"
    properties:
      hasBeenCreator:
        type: "boolean"
      autopublishAllowed:
        type: "boolean"
  JsonOkResponseInstagramAutoPublishProperties:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/InstagramAutoPublishProperties"
  JsonOkListResponseScheduledPostEventDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostEventDto"
  ScheduledPostEventDto:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      postUuid:
        type: "string"
      userId:
        type: "integer"
        format: "int32"
      agencyId:
        type: "integer"
        format: "int32"
      userName:
        type: "string"
      type:
        type: "string"
      version:
        type: "integer"
        format: "int32"
      date:
        $ref: "#/definitions/DateTimeInfo"
      metadata:
        type: "object"
  JsonOkListResponseScheduledPostNote:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ScheduledPostNote"
  ScheduledPostNoteRequest:
    type: "object"
    properties:
      content:
        type: "string"
  JsonOkResponseScheduledPostNote:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/ScheduledPostNote"
  JsonOkListResponseLibraryPostEventDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/LibraryPostEventDto"
  LibraryPostEventDto:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      postId:
        type: "integer"
        format: "int64"
      userId:
        type: "integer"
        format: "int32"
      agencyId:
        type: "integer"
        format: "int32"
      agencyUserId:
        type: "integer"
        format: "int32"
      userName:
        type: "string"
      type:
        type: "string"
      version:
        type: "integer"
        format: "int32"
      date:
        $ref: "#/definitions/DateTimeInfo"
      metadata:
        type: "object"
  JsonOkListResponseLibraryPostDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/LibraryPostDto"
  JsonOkResponseLibraryPostDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/LibraryPostDto"
  IpFiltersResponse:
    type: "object"
    properties:
      ip:
        type: "string"
      filtered:
        type: "boolean"
  JsonOkResponseIpFiltersResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/IpFiltersResponse"
  BlueskyData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
  Brand:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      ownerUserId:
        type: "integer"
        format: "int32"
      label:
        type: "string"
      title:
        type: "string"
      description:
        type: "string"
      image:
        type: "string"
      networksData:
        $ref: "#/definitions/NetworksData"
      isShared:
        type: "boolean"
      ownerUsername:
        type: "string"
      whiteLabelData:
        $ref: "#/definitions/WhiteLabelData"
      hash:
        type: "string"
      version:
        type: "integer"
        format: "int64"
      deleteDate:
        $ref: "#/definitions/DateTimeInfo"
      deleted:
        type: "boolean"
      joinDate:
        $ref: "#/definitions/DateTimeInfo"
      firstConnectionDate:
        $ref: "#/definitions/DateTimeInfo"
      lastResolvedInboxMessageTimestamp:
        type: "integer"
        format: "int64"
      lastReadInboxMessageTimestamp:
        type: "integer"
        format: "int64"
      timezone:
        type: "string"
      availableConnectors:
        type: "array"
        items:
          type: "string"
      brandRole:
        $ref: "#/definitions/BrandRole"
      isDemo:
        type: "boolean"
      properties:
        $ref: "#/definitions/BrandProperties"
  BrandProperties:
    type: "object"
    properties:
      customEmail:
        type: "string"
      additionalNotificationAddresses:
        type: "array"
        uniqueItems: true
        items:
          type: "string"
      colors:
        $ref: "#/definitions/Colors"
      trialExcluded:
        type: "string"
      engagementRatio:
        type: "integer"
        format: "int32"
  Colors:
    type: "object"
    properties:
      blue:
        type: "string"
      teal:
        type: "string"
      pink:
        type: "string"
      yellow:
        type: "string"
      purple:
        type: "string"
      cyan:
        type: "string"
      red:
        type: "string"
      green:
        type: "string"
      slate:
        type: "string"
      charcoal:
        type: "string"
      lightYellow:
        type: "string"
      darkYellow:
        type: "string"
  FacebookAdsData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
  FacebookData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      userId:
        type: "string"
  GbpData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      locationdId:
        type: "string"
      address:
        type: "string"
      profileURL:
        type: "string"
  InstagramData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      connectionType:
        type: "string"
        enum:
        - "BUSINESS"
        - "FACEBOOK_LOGIN"
  JsonOkResponseBrand:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/Brand"
  LinkedinData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      userId:
        type: "string"
      tokenExpiration:
        type: "string"
      profileURL:
        type: "string"
      accountType:
        type: "string"
        enum:
        - "BUSINESS"
        - "PERSONAL"
  NetworksData:
    type: "object"
    properties:
      webData:
        $ref: "#/definitions/WebData"
      facebookData:
        $ref: "#/definitions/FacebookData"
      instagramData:
        $ref: "#/definitions/InstagramData"
      threadsData:
        $ref: "#/definitions/ThreadsData"
      twitterData:
        $ref: "#/definitions/TwitterData"
      blueskyData:
        $ref: "#/definitions/BlueskyData"
      linkedinData:
        $ref: "#/definitions/LinkedinData"
      pinterestData:
        $ref: "#/definitions/PinterestData"
      tiktokData:
        $ref: "#/definitions/TikTokData"
      gbpData:
        $ref: "#/definitions/GbpData"
      youtubeData:
        $ref: "#/definitions/YoutubeData"
      twitchData:
        $ref: "#/definitions/TwitchData"
      facebookAdsData:
        $ref: "#/definitions/FacebookAdsData"
      googleAdsData:
        $ref: "#/definitions/GoogleAdsData"
      tiktokAdsData:
        $ref: "#/definitions/TikTokAdsData"
  PinterestData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      accountType:
        type: "string"
        enum:
        - "BUSINESS"
        - "PERSONAL"
  ThreadsData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      displayName:
        type: "string"
  TikTokAdsData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      userId:
        type: "string"
  TikTokData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      accountType:
        type: "string"
        enum:
        - "BUSINESS"
        - "PERSONAL"
      businessTokenExpiration:
        type: "string"
      profileURL:
        type: "string"
  TwitchData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
  TwitterData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
      hasOAuth2Token:
        type: "boolean"
      twitterSubscriptionType:
        type: "string"
  WebData:
    type: "object"
    properties:
      url:
        type: "string"
      feedRss:
        type: "string"
  WhiteLabelData:
    type: "object"
    properties:
      whiteLabelLink:
        type: "string"
      analyticModeWhitelabelLink:
        type: "string"
      whiteLabelAlias:
        type: "string"
      isWhiteLabel:
        type: "boolean"
      isWhiteLabelOnlyRead:
        type: "boolean"
  YoutubeData:
    type: "object"
    properties:
      username:
        type: "string"
      providerUserId:
        type: "string"
      picture:
        type: "string"
  BrandLite:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      ownerUserId:
        type: "integer"
        format: "int32"
      label:
        type: "string"
      title:
        type: "string"
      description:
        type: "string"
      image:
        type: "string"
      ownerUsername:
        type: "string"
      hash:
        type: "string"
      joinDate:
        $ref: "#/definitions/DateTimeInfo"
      firstConnectionDate:
        $ref: "#/definitions/DateTimeInfo"
      timezone:
        type: "string"
      brandRole:
        $ref: "#/definitions/BrandRole"
      engagementRatio:
        type: "integer"
        format: "int32"
      networksData:
        $ref: "#/definitions/NetworksData"
      isShared:
        type: "boolean"
  JsonOkListResponseBrandLite:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/BrandLite"
  EngagementRatioValue:
    type: "object"
    required:
    - "value"
    properties:
      value:
        type: "integer"
        format: "int32"
  BrandFeed:
    type: "object"
    properties:
      feedUrl:
        type: "string"
  JsonOkResponseBrandFeed:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/BrandFeed"
  InstagramFeedMedia:
    type: "object"
    properties:
      id:
        type: "string"
      blogId:
        type: "integer"
        format: "int32"
      username:
        type: "string"
      fbPostId:
        type: "string"
      type:
        type: "string"
      publishedAt:
        $ref: "#/definitions/DateTimeInfo"
      content:
        type: "string"
      imageUrl:
        type: "string"
      mediaUrl:
        type: "string"
  JsonOkListResponseInstagramFeedMedia:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/InstagramFeedMedia"
  BrandProfile:
    type: "object"
    properties:
      username:
        type: "string"
      picture:
        type: "string"
  FacebookConnectionRequest:
    type: "object"
    properties:
      token:
        type: "string"
  Country:
    type: "object"
    properties:
      isoCode:
        type: "string"
      name:
        type: "string"
      isEUCountry:
        type: "boolean"
  JsonOkListResponseCountry:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Country"
  JsonOkListResponseState:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/State"
  State:
    type: "object"
    properties:
      isoCode:
        type: "string"
      name:
        type: "string"
  AvailableNetworks:
    type: "object"
  CreditCardAccount:
    type: "object"
    properties:
      creditCardToken:
        type: "string"
      currency:
        type: "string"
      brandCard:
        type: "string"
      endCreditNumber:
        type: "string"
      cardExpYear:
        type: "integer"
        format: "int64"
      cardExpMonth:
        type: "integer"
        format: "int64"
      selected:
        type: "boolean"
      provider:
        type: "string"
      availableNetworks:
        $ref: "#/definitions/AvailableNetworks"
  JsonOkResponseUserPaymentMethods:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/UserPaymentMethods"
  PayPalAccount:
    type: "object"
    properties:
      payPalToken:
        type: "string"
      email:
        type: "string"
      imageUrl:
        type: "string"
      selected:
        type: "boolean"
  UserPaymentMethods:
    type: "object"
    properties:
      creditCards:
        type: "array"
        items:
          $ref: "#/definitions/CreditCardAccount"
      payPalAccounts:
        type: "array"
        items:
          $ref: "#/definitions/PayPalAccount"
  AddonData:
    type: "object"
    properties:
      id:
        type: "string"
        enum:
        - "TWITTER"
      price:
        type: "number"
        format: "float"
      purchasable:
        type: "boolean"
  JsonOkResponseSubscription:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/Subscription"
  TaxData:
    type: "object"
    properties:
      vatRate:
        type: "number"
        format: "double"
      company:
        type: "string"
      country:
        type: "string"
      state:
        type: "string"
      address:
        type: "string"
      vatNumber:
        type: "string"
      addOn:
        type: "string"
  JsonOkListResponseSubscriptionPlan:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/SubscriptionPlan"
  SubscriptionChangeRequest:
    type: "object"
    required:
    - "updateOperation"
    properties:
      updateOperation:
        type: "string"
      couponCode:
        type: "string"
      planId:
        type: "string"
      proration:
        type: "boolean"
      currency:
        type: "string"
      provider:
        type: "string"
      paymentMethodToken:
        type: "string"
      addons:
        type: "object"
        additionalProperties:
          type: "integer"
          format: "int32"
  CreateSubscriptionRequest:
    type: "object"
    properties:
      provider:
        type: "string"
      paymentMethodToken:
        type: "string"
      planId:
        type: "string"
      couponCode:
        type: "string"
      taxData:
        $ref: "#/definitions/TaxData"
      addons:
        type: "object"
        additionalProperties:
          type: "integer"
          format: "int32"
  SubscriptionCancelRequest:
    type: "object"
    properties:
      message:
        type: "string"
  Coupon:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int32"
      code:
        type: "string"
      amount:
        type: "number"
        format: "float"
      billingCycles:
        type: "integer"
        format: "int32"
      expiration:
        $ref: "#/definitions/DateTimeInfo"
      maxDiscounts:
        type: "integer"
        format: "int32"
      forNewUsers:
        type: "boolean"
      hashtagsBalance:
        type: "integer"
        format: "int32"
      ownerId:
        type: "integer"
        format: "int32"
      label:
        type: "string"
      discountsCount:
        type: "integer"
        format: "int32"
      revenue:
        type: "number"
        format: "double"
      creation:
        $ref: "#/definitions/DateTimeInfo"
      user:
        $ref: "#/definitions/User"
      percentage:
        type: "boolean"
      trial:
        type: "integer"
        format: "int32"
      enabled:
        type: "boolean"
      assignedTeamCouponTracking:
        type: "string"
      appliedAt:
        $ref: "#/definitions/DateTimeInfo"
  CouponResult:
    type: "object"
    properties:
      finalPriceWithoutTaxes:
        type: "number"
        format: "double"
      isFreeCoupon:
        type: "boolean"
      coupon:
        $ref: "#/definitions/Coupon"
  JsonOkResponseCouponResult:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/CouponResult"
  OnboardingData:
    type: "object"
    properties:
      required:
        type: "boolean"
      finished:
        type: "boolean"
      buyerPersona:
        type: "string"
      size:
        type: "string"
      goal:
        type: "array"
        items:
          type: "string"
      networks:
        type: "array"
        items:
          type: "string"
      partnersOnboardings:
        type: "array"
        items:
          type: "object"
          additionalProperties:
            type: "object"
  JsonOkResponseFloat:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "number"
        format: "float"
  Application:
    type: "object"
    properties:
      name:
        type: "string"
      id:
        type: "string"
  JsonOkListResponseTimezone:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/Timezone"
  Timezone:
    type: "object"
    properties:
      name:
        type: "string"
  JsonOkResponseUser:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/User"
  DeleteUserRequest:
    type: "object"
    properties:
      reasonMessage:
        type: "string"
  UpdateUserRequest:
    type: "object"
    properties:
      name:
        type: "string"
      lastName:
        type: "string"
      language:
        type: "string"
      timezone:
        type: "string"
      accountLogo:
        type: "string"
      headerLogo:
        type: "string"
      company:
        type: "string"
      country:
        type: "string"
      state:
        type: "string"
      address:
        type: "string"
      vatNumber:
        type: "string"
      sendToAlternativeEmail:
        type: "boolean"
      alternativeEmail:
        type: "string"
      marketingNotifications:
        type: "boolean"
      billEmails:
        type: "array"
        items:
          type: "string"
      beta:
        type: "boolean"
      locked:
        type: "boolean"
      enabled:
        type: "boolean"
      onboarding:
        $ref: "#/definitions/OnboardingData"
      firstDayOfTheWeek:
        type: "string"
      whiteLabelIntegrator:
        type: "boolean"
  JsonOkResponseUserCredentials:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/UserCredentials"
  UserCredentials:
    type: "object"
    properties:
      userName:
        type: "string"
  UpdateUserCredentialsRequest:
    type: "object"
    properties:
      userName:
        type: "string"
      oldPassword:
        type: "string"
      password:
        type: "string"
      recoveryToken:
        type: "string"
  JsonOkResponseSavedText:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/SavedText"
  SavedText:
    type: "object"
    required:
    - "id"
    properties:
      id:
        type: "integer"
        format: "int32"
      blogId:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      title:
        type: "string"
      text:
        type: "string"
      deleted:
        type: "boolean"
      tags:
        type: "array"
        items:
          type: "string"
      scope:
        type: "string"
  SavedTextRequest:
    type: "object"
    properties:
      title:
        type: "string"
      text:
        type: "string"
      tags:
        type: "array"
        items:
          type: "string"
      scope:
        type: "string"
  JsonOkListResponseSavedTextWithPermissions:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/SavedTextWithPermissions"
  SavedTextWithPermissions:
    type: "object"
    required:
    - "id"
    properties:
      id:
        type: "integer"
        format: "int32"
      blogId:
        type: "integer"
        format: "int32"
      userId:
        type: "integer"
        format: "int32"
      title:
        type: "string"
      text:
        type: "string"
      deleted:
        type: "boolean"
      tags:
        type: "array"
        items:
          type: "string"
      scope:
        type: "string"
      canDelete:
        type: "boolean"
      canEdit:
        type: "boolean"
  JsonOkListResponseStTagCount:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/StTagCount"
  StTagCount:
    type: "object"
    properties:
      tag:
        type: "string"
      tagCount:
        type: "integer"
        format: "int32"
  RecoveryChangeRequest:
    type: "object"
    properties:
      enabled:
        type: "boolean"
      password:
        type: "string"
  ApiConsumptionData:
    type: "object"
  JsonOkListResponseApiConsumptionData:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/ApiConsumptionData"
  JsonOkResponseTrialEligibilityResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/TrialEligibilityResponse"
  TrialEligibilityResponse:
    type: "object"
    properties:
      eligible:
        type: "boolean"
  JsonOkResponseTrialInfoResponse:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/TrialInfoResponse"
  TrialInfoResponse:
    type: "object"
    properties:
      userId:
        type: "integer"
        format: "int32"
      startDate:
        $ref: "#/definitions/DateTimeInfo"
      endDate:
        $ref: "#/definitions/DateTimeInfo"
      pageId:
        type: "string"
      pageName:
        type: "string"
      isActive:
        type: "boolean"
  JsonOkResponseLoginInfo:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        $ref: "#/definitions/LoginInfo"
  LoginInfo:
    type: "object"
    properties:
      token:
        type: "string"
      loginUrl:
        type: "string"
  JsonOkListResponseLegalTermDto:
    type: "object"
    properties:
      metadata:
        type: "object"
      page:
        $ref: "#/definitions/JsonPaging"
      data:
        type: "array"
        items:
          $ref: "#/definitions/LegalTermDto"
  LegalTermDto:
    type: "object"
    properties:
      type:
        type: "string"
      version:
        type: "string"
      versionDate:
        $ref: "#/definitions/DateTimeInfo"
      description:
        type: "string"
      acceptanceDeadline:
        $ref: "#/definitions/DateTimeInfo"
  ContractEventRequest:
    type: "object"
    properties:
      event:
        type: "string"
