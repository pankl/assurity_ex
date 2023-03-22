from Helpers.ConfigReader import ReadConfiguration 

configuration = ReadConfiguration()
baseUri = configuration.getValueFromConfig('BaseUri')
PromotionName = configuration.getValueFromConfig('PromotionName')
DescriptionSubString = configuration.getValueFromConfig('DescriptionSubString')
