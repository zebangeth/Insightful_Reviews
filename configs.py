# --- System Config ---

# --- Model Selection ---
OPENAI_GPT3 = "gpt-3.5-turbo-16k-0613"
CLAUDE_DEFAULT = "claude-2"
CLAUDE_INSTANT = "claude-instant-1"
CLAUDE_2 = "claude-2"

# 单次读取评价条数上限
REVIEW_NUM_CAP = 300
OPENAI_CAP = 75

# USER_POSITION = ["暂不选择", "👨🏻‍💻 电商运营", "🤵🏻‍♂️ 电商客服", "👩🏻‍🔬 产品研发", "👩🏻‍🔧 生产/质量控制", "✈️ 物流/供应链"]
# ANALYSIS_FOCUS = ["暂不选择", "⚙️ 产品功能", "💎 产品质量", "🎨 产品外观", "🖐️ 使用体验", "💰 价格合理性", "💳 客户服务与下单体验", "📦 包装与物流"]

USER_POSITION = {
    "zh": ["暂不选择", "👨🏻‍💻 电商运营", "🤵🏻‍♂️ 电商客服", "👩🏻‍🔬 产品研发", "👩🏻‍🔧 生产/质量控制", "✈️ 物流/供应链"],
    "en": ["None Selected", "👨🏻‍💻 E-commerce Operations", "🤵🏻‍♂️ Customer Service", "👩🏻‍🔬 Product R&D", "👩🏻‍🔧 Production/QC", "✈️ Logistics/Supply Chain"]
}
ANALYSIS_FOCUS = {
    "zh": ["暂不选择", "⚙️ 产品功能", "💎 产品质量", "🎨 产品外观", "🖐️ 使用体验", "💰 价格合理性", "💳 客户服务与下单体验", "📦 包装与物流"],
    "en": ["None Selected", "⚙️ Product Features", "💎 Product Quality", "🎨 Design & Appearance", "🖐️ User Experience", "💰 Pricing", "💳 Customer Service & Ordering", "📦 Packaging & Logistics"]
}

# ---  Prompt Library ---
FOCUS_TO_PROMPT = {
    "⚙️ 产品功能": "产品的功能特性，如：产品的主要功能，功能的实用性以及客户对功能的反应。",
    "💎 产品质量": "探讨产品的质量问题，如：产品的耐用性，质量稳定性，以及客户对产品质量的反馈。",
    "🎨 产品外观": "产品的外观设计，如：产品的外观、颜色，形状，尺寸，以及客户对外观设计的反馈。",
    "🖐️ 使用体验": "客户对产品使用体验的反馈，如：产品的使用便利性，舒适性以及客户在使用过程中遇到的问题。",
    "💰 价格合理性": "探讨产品的价格问题。如：产品的价格是否合理，价格与产品的价值是否匹配，以及客户对产品价格的反馈。",
    "💳 客户服务与下单体验": "客服和下单体验，如：在线客服人员的响应速度，服务质量，客服专业性，下单流程的便利性以及客户的其他反馈。",
    "📦 包装与物流": "产品的包装和物流问题，如：产品的包装是否完好、包装的外观设计、物流速度等，以及客户对包装和物流的反馈。",
}

POSITION_TO_PROMPT = {
    "👨🏻‍💻 电商运营": "电商运营经理的角度分析，注意任何可能影响产品销量和客户满意度的因素，如产品受欢迎程度、销售策略、定价等，以及客户的反馈和建议。",
    "🤵🏻‍♂️ 电商客服": "客户服务经理的角度分析，重点关注客户对客服服务过程的反馈，如客服服务质量、响应速度、专业性、客户问题、投诉情况等，并给出完整的分析总结。",
    "👩🏻‍🔬 产品研发": "产品研发经理的角度分析，关注客户对产品功能和设计上优缺点的反馈，如产品功能、用户体验、产品优化需求等，并给出完整的分析总结。这将有助于产品的优化和改进。",
    "👩🏻‍🔧 生产/质量控制": "生产和质量控制部门经理的角度分析，请重点关注客户对产品质量的反馈，如产品质量问题、产品瑕疵等，并给出完整的分析总结。",
    "✈️ 物流/供应链": "物流和供应链部门经理的角度分析，请注意客户对产品包装和物流的反馈，如包装物流问题、物流速度和物流体验等，并给出完整的分析总结。",
}

# --- Container Config ---
CONTENT_COL_CONFIG = [1, 6, 1]