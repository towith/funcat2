# -*- coding: utf-8 -*-
'''
Created on 2021-05-17

@author: p19992003
'''
import numpy as np
from turtle import Turtle


class Turtle(object):
    '''
    海龟法则
    《金融评论》曾发表过一篇论文，里面刊载了十年间对二十多种技术型交易系统的测试和研究，最终得出了结论，周规则名列榜首，仅随其后的是移动平均线。同时期，理查德·丹尼斯（Richard Dennis）创办了举世轰动的“海龟交易班”，“龟儿”们创造了四年年均复利八十的收益，而《海龟交易法则》中的具体操作信号正是周规则。对于移动平均线，大家早已熟，那么周规则是什么呢？为什么它如此优秀，就连世界上最顶级的交易员都在使用它？
    周规则是由理查德·唐迁（Richard Donchian）发明的，它是一种追随趋势的自动交易系统。最初它以四周的形式出现。以周规则为基础的交易系统十分简单，下面以四周规则为例，讲述它的使用方法。
    四周规则的使用方法：
    1、只要价格超出前四周内的最高价，就平掉空头仓位并做多；
    2、只要价格跌破前四周内的最低价，就平掉多头仓位并做空。
    交易者可以在四周规则的基础上，对其进行优化，为了避免在无趋势时产生的错误开仓信号和尽量的保护手中利润，可以将四周规则用于开仓，而将二周规则用于平仓。同样周规则也适用于任何时间周期，同时，它不仅可以当作交易系统使用，还可以当作辨别趋势是否反转的工具。如果你是一个系统交易者，那么通过优化周规则和在其基础上进行交易是最好的选择，因为它已被证明具备在任何市场中获利的能力。最后需要指出的是，使用周规则应该始终如一按照它的指示去操作，往往一年甚至几年的利润就在一次信号之中。
    以周期理论为主要工具的分析者认为，市场运动的最终线索就在其运行周期上。不可否认，时间周期的研究成果，为我们的测市手段增加了时间维度。作为理论，经过不断丰富和发展之后，变得繁复而深奥是可以理解的；作为手段，其存在和发展必定有其特殊理由，但任何一种技术都会因其自身利弊、得失而无法概全。在这里，笔者力求以简练的语言和朋友们交流其核心内容的应用心得。
　　通常，周期分析者认为，波谷比波峰可靠，所以周期长度的度量都是从波谷到波谷进行的，原因大概是绝大多数周期的变异出现在波峰上，也就是说波峰的形成比较复杂，因而认为波谷更可靠些。从实际应用结果来看，在牛市中周期分析远比在熊市中表现优异。原因何在，笔者认为，这与周期理论研究倾向于关注底部有关。同时笔者发现，在牛市中，波谷比波峰形成或驻留的时间相对较短，而波峰因常 出现强势整理的态势，变得复杂起来，所以较难把握。在熊市中则相反，因为市态较弱，市场常以整理形态取代反弹，所以波峰比波谷形成时间要短，易于发现。在运用周期理论测市的时候，牛市中以波谷法度量较为准确，熊市中以波峰法度量胜算更高些。笔者之所以倾向于度量构筑时间较短的形态，是因为这样的形态比较容易判别，预测时间目标与实际发生时间的偏差较小。有兴趣的朋友不妨一试。
　　在决定使用峰测法还是谷测法度量的时候，除了使用趋势线来筛选之外，还有一种方法也可以给您很大的帮助，那就是先观察上一层次周期中，波峰是向周期时间中线左移还是右移，即一个涨跌周期如是40天，波峰是向20天之前移还是向20天之后移，左移看跌，右移看涨。看跌时用峰测法，看涨时用谷测法。波峰左移和右移作为辅助工具之一，适用于任何趋势和长度的周期。周期理论中四个重要的基本原理：叠加原理、谐波原理、同步原理、比例原理，以及两个通则原理：变通原理、基准原理，本文中不再赘述了。
　　关于时间周期，则不能不提神奇的菲波纳契数列1、1、2、3、5、 8、12、21、34、55、89、144……，这组数字之间的关系，有书籍专论，本文不详细述及。由于它是波浪理论的基础，波浪理论与周期理论也颇有渊源，在运用周期理论测市的时候，不论是从重要的市场顶部只是底部起向未来数算，得出菲波纳契时间目标，这些日子都可能 意味着成为市场重要的转折点。在这些时间窗口，如何取得交易信号，还需辅以其他技术手段以验证。对于神奇数字，笔者从江恩理论及其小说中体会到一种默契，江恩将“7”及其倍数的周期视作重要的转折点。笔者发现，如果这个数字是菲波纳契数×7，那这个数字更神奇。 我们如何理解“7”这个数字呢，在江恩眼里，上帝用７天创造了世界， 因此“7”是一个完整的数字；在圣经中，人类最大的敌人-死亡的恐 俱也是可以克服的，耶酥在死后的第３天站起来，第7天复活，这意昧着７天是一个周期，“3”是菲波纳契数字，就是“4”也相当不平凡。 地球自转一周为360度，每４分钟旋转1度，因此，最短的循环可以是4 分钟，地球启转一周需再24小时，也是4的倍数，所以４×７天的周期 也是一个很重要的短期周期。而上述一系列数字构成了价格变化的时间窗，一旦市场进入了时间窗，我们还须依靠其他技术工具做过滤器， 如摆动指标KDJ、W%、RSI等，过滤伪杂信息来判断转折点的出现，并得出交易信号。
　　需要特别指出的是，在运用周期理论、波浪理论菲波纳契数列的时候，要注意它们都是以群体心理为基础的，也就是说市场规模越大，参与的人数越多，就越符合上述理论，比如股指远比个股符合上述理论，况且波浪理论本意也是应用于股市平均指数的。

    我们知道增加盈利的手段不外乎是开源节流，这里我先从节流挖潜力。由于时候验证是很难的，难在不加已知结果下的主观影响。因此新加入的条件一定要中性，可操作，不能事后诸葛亮。我在Week图中仅仅加入了两条EMA，然后规定了下面几条限制：
    1. 上升的EMA下方不开新的空单掉头；
    2. 下降的EMA上方不开新的多单掉头；
    3. 典型双顶模式下不做相反的单子掉头。

    周规则广泛应用于任何的投资市场中，在期货市场中应用较多，同样也适合于股票市场，夏蕊看股经过研究，总结出了在股票市场中的周规则。

股票投资的周规则：

周规则一：
只要本周的收盘价超出前四周内的最高价，就可买进股票做多。
只要本周的收盘价低于前两周内的最低价，就要卖出股票做空。

周规则二：
只要本周的收盘价超出前三周内的最高的收盘价或开盘价，就可买进股票做多。
只要本周的收盘价低于前三周内的最低的收盘价或开盘价，就可卖出股票做空。
    '''

    def __init__(self):
        '''
        '''
        pass

    @classmethod
    def default_quantity(cls):
        """返回四周规则最高价、最低价基准；
        e.g. return CLOSE, CLOSE 表示最高收盘价 最低收盘价作为最高价，最低价的比较基准
        """
        from funcat.api import CLOSE, HIGH, LOW
        return CLOSE, CLOSE

    @classmethod
    def four_week_qty(cls, high_series=None, low_series=None, high_n:int=20, low_n:int=20):
        """四周规则;日线级别
        参数high_series,low_series为None时，序列默认为从_default_quantity()获取（此处为CLOSE， CLOSE）
        Args:
            high_series: 价格（成交量）序列）; 用于取周期n内的最高价（成交量）
            low_series: 价格（成交量）序列）; 用于取周期n内的最低价（成交量）
            high_n: 计算最高价的周期数（默认：20）;
            low_n : 计算最低价的周期数（默认：20）;
        Returns：
            截取最高价、最低价
        """
        from funcat.api import LLV, HHV
        if high_series is None:
            # 没有参数时，序列默认为从_default_quantity()获取（此处为CLOSE， CLOSE）
            high_series, low_series = cls.default_quantity()
        last_high = HHV(high_series, high_n)
        last_low = LLV(low_series, low_n)
        return last_high, last_low

    @classmethod
    def four_week(cls, high_series=None, low_series=None, high_n:int=20, low_n:int=20):
        """四周规则的使用方法：
        1、只要价格超出前四周内的最高价，就平掉空头仓位并做多；
        2、只要价格跌破前四周内的最低价，就平掉多头仓位并做空。
        """
        from funcat.api import LLV, HHV, REF, IF, \
            NumericSeries
        if high_series is None:
            high_series, low_series = cls.default_quantity()
        last_high, last_low = cls.four_week_qty(high_series, low_series, high_n, low_n)
        hh = IF(high_series > REF(last_high, 1), 1, 0)
        ll = IF(low_series < REF(last_low, 1), -1, 0)
        return  NumericSeries(np.append(np.array([np.nan]), hh.series)), NumericSeries(np.append(np.array([np.nan]), ll.series))


class TurtleUsingHighLow(Turtle):

    @classmethod
    def default_quantity(cls):
        """返回四周规则最高价、最低价基准；
        e.g. return HIGH, LOW , 表示最高价 最低价作为最高价，最低价的比较基准
        """
        from funcat.api import HIGH, LOW
        return HIGH, LOW


FOURWEEKQTY = Turtle.four_week_qty
FOURWEEK = Turtle.four_week