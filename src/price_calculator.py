import logging

logger = logging.getLogger(__name__)

class PriceCalculator:
    """
    修复后的价格计算器：
    - 校验输入不能为负数（抛出 ValueError）
    - 计算 final_price 后，如果小于 0 则调整为 0 并记录警告
    - 中文注释用于教学说明
    """
    def calculate_final_price(self, original_price, discount_coupon, points_value):
        # 参数基本校验：不得为负
        if original_price < 0 or discount_coupon < 0 or points_value < 0:
            raise ValueError("价格和优惠金额不能为负数")

        # 计算最终价格
        final_price = original_price - discount_coupon - points_value

        # 如果计算结果为负，防止倒贴，调整为 0 并记录日志
        if final_price < 0:
            logger.warning(
                "优惠金额超过商品价格（original=%s, coupon=%s, points=%s），已将最终价格调整为 0",
                original_price, discount_coupon, points_value
            )
            final_price = 0

        return final_price
