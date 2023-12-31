from configs import REVIEW_NUM_CAP, OPENAI_CAP

model_comparison_table = {
    "en": f"""
    <table style="width:100%; border-collapse: collapse; border: 1px solid #dddddd; border-radius: 10px; margin-bottom: 15px;">
    <tr style="background-color: #F0F2F6;">
        <th style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Model Name</th>
        <th style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Analysis Capacity</th> 
        <th style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Analysis Quality</th>
        <th style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Analysis Speed</th>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;"><strong>gpt-3.5</strong></td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Up to {OPENAI_CAP} reviews</td> 
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">High</td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Medium</td>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;"><strong>claude-instant</strong></td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Up to {REVIEW_NUM_CAP} reviews</td> 
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Medium</td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Fastest</td>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;"><strong>claude-2</strong></td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Up to {REVIEW_NUM_CAP} reviews</td> 
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">High</td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">Slowest</td>
    </tr>
    </table>
    """,
    "zh": f"""
    <table style="width:100%; border-collapse: collapse; border: 1px solid #dddddd; border-radius: 10px; margin-bottom: 15px;">
    <tr style="background-color: #F0F2F6;">
        <th style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">模型名称</th>
        <th style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">分析数量</th> 
        <th style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">分析质量</th>
        <th style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">分析速度</th>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;"><strong>gpt-3.5</strong></td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">最多{OPENAI_CAP}条评论</td> 
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">高</td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">中等</td>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;"><strong>claude-instant</strong></td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">最多{REVIEW_NUM_CAP}条评论</td> 
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">中</td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">最快</td>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;"><strong>claude-2</strong></td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">最多{REVIEW_NUM_CAP}条评论</td> 
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">高</td>
        <td style="border: 1px solid #dddddd; padding: 5px; text-align: left; color: #31333F;">最慢</td>
    </tr>
    </table>
    """
}
    