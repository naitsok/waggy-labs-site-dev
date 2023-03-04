from waggylabs.blocks.base_body import BaseBodyBlock
from waggylabs.blocks.page_info import PageInfoBlock
from waggylabs.blocks.post_meta import PostMetaBlock
from waggylabs.blocks.post_series import PostSeriesBlock


class PostBodyBlock(BaseBodyBlock):
    """Post body block has specific additional blocks."""
    post_meta = PostMetaBlock()
    page_info = PageInfoBlock()
    post_series = PostSeriesBlock()
    
    def render(self, value, context):
        # if post_meta and page_info blocks are at the end of body
        # before them references must be rendered
        page_body = []
        info_meta = []
        for idx, block in enumerate(value):
            if (idx >= len(value) - 2) and \
                (value.raw_data[-1]['type'] in ['post_meta', 'page_info']) and \
                (block.block_type in ['post_meta', 'page_info']):
                info_meta.append(block)
            else:
                page_body.append(block)
                
        value = {
            'body': page_body,
            'info_meta': info_meta,
        }
        
        return super().render(value, context)
    
    class Meta:
        block_counts = {
            'post_meta': { 'max_num': 1 },
            'page_info': { 'max_num': 1 },
        }