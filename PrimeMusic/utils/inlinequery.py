from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = [
    InlineQueryResultArticle(
        title="Pause Stream",
        description="Pause the current playout on group call.",
        thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
        input_message_content=InputTextMessageContent("/pause"),
    ),
    InlineQueryResultArticle(
        title="Resume Stream",
        description="Resume the ongoing playout on group call.",
        thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
        input_message_content=InputTextMessageContent("/resume"),
    ),
    InlineQueryResultArticle(
        title="Mute Stream",
        description="Mute the ongoing playout on group call.",
        thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
        input_message_content=InputTextMessageContent("/mute"),
    ),
    InlineQueryResultArticle(
        title="Unmute Stream",
        description="Unmute the ongoing playout on group call.",
        thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
        input_message_content=InputTextMessageContent("/unmute"),
    ),
    InlineQueryResultArticle(
        title="Skip Stream",
        description="Skip to next track. | For Specific track number: /skip [number] ",
        thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
        input_message_content=InputTextMessageContent("/skip"),
    ),
    InlineQueryResultArticle(
        title="End Stream",
        description="Stop the ongoing playout on group call.",
        thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
        input_message_content=InputTextMessageContent("/end"),
    ),
    InlineQueryResultArticle(
        title="Shuffle Stream",
        description="Shuffle the queued tracks list.",
        thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
        input_message_content=InputTextMessageContent("/shuffle"),
    ),
    InlineQueryResultArticle(
        title="Seek Stream",
        description="Seek the ongoing stream to a specific duration.",
        thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
        input_message_content=InputTextMessageContent("/seek 10"),
    ),
    InlineQueryResultArticle(
        title="Loop Stream",
        description="Loop the current playing music. | Usage: /loop [enable|disable]",
        thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
        input_message_content=InputTextMessageContent("/loop 3"),
    ),
]
