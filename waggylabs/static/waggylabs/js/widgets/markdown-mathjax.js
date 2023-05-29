function getMathJaxMathCommands() {
    return [
    "\\_", "\\,", "\\;", "\\:", "\\!", "\\{", "\\}", "\\\\", "\\&", "\\#", "\\%", "\\>", "\\|", "\\$", "\\above", "\\abovewithdelims", "\\Aboxed", "\\abs", "\\absolutevalue", 
    "\\acomm", "\\acos", "\\acosecant", "\\acosine", "\\acot", "\\acotangent", "\\acsc", "\\acute", "\\adjustlimits", "\\admat", "\\aleph", "\\alpha", "\\alwaysDashedLine", 
    "\\alwaysNoLine", "\\alwaysRootAtBottom", "\\alwaysRootAtTop", "\\alwaysSingleLine", "\\alwaysSolidLine", "\\amalg", "\\And", "\\angle", "\\anticommutator", 
    "\\antidiagonalmatrix", "\\approx", "\\approxeq", "\\arccos", "\\arccosecant", "\\arccosine", "\\arccot", "\\arccotangent", "\\arccsc", "\\arcsec", "\\arcsecant", 
    "\\arcsin", "\\arcsine", "\\arctan", "\\arctangent", "\\arg", "\\array", "\\ArrowBetweenLines", "\\arrowvert", "\\Arrowvert", "\\asec", "\\asecant", "\\asin", "\\asine", 
    "\\ast", "\\asymp", "\\atan", "\\atangent", "\\atop", "\\atopwithdelims", "\\AXC", "\\Axiom", "\\AxiomC", 
    "\\backepsilon", "\\backprime", "\\backsim", "\\backsimeq", "\\backslash", "\\bar", "\\barwedge", "\\Bbb", "\\Bbbk", "\\bbFont", "\\bbox", "\\bcancel", 
    "\\because", /* "\\begin", */ "\\beta", "\\beth", "\\between", "\\bf", "\\BIC", "\\big", "\\Big", "\\bigcap", "\\bigcirc", "\\bigcup", "\\bigg", "\\Bigg", 
    "\\biggl", "\\Biggl", "\\biggm", "\\Biggm", "\\biggr", "\\Biggr", "\\bigl", "\\Bigl", "\\bigm", "\\Bigm", "\\bigodot", "\\bigoplus", "\\bigotimes", "\\bigr", 
    "\\Bigr", "\\bigsqcup", "\\bigstar", "\\bigtimes", "\\bigtriangledown", "\\bigtriangleup", "\\biguplus", "\\bigvee", "\\bigwedge", "\\BinaryInf", "\\BinaryInfC", 
    "\\binom", "\\blacklozenge", "\\blacksquare", "\\blacktriangle", "\\blacktriangledown", "\\blacktriangleleft", "\\blacktriangleright", "\\bmod", "\\bmqty", 
    "\\boldsymbol", "\\bot", "\\bowtie", "\\Box", "\\boxdot", "\\boxed", "\\boxminus", "\\boxplus", "\\boxtimes", "\\bqty", "\\Bqty", "\\bra", "\\Bra", "\\brace", 
    "\\bracevert", "\\brack", "\\braket", "\\Braket", "\\breve", "\\buildrel", "\\bullet", "\\bumpeq", "\\Bumpeq", "\\cal", "\\cancel", "\\cancelto", "\\cap", "\\Cap", 
    "\\cases", "\\cdot", "\\cdotp", "\\cdots", "\\ce", "\\cellcolor", "\\celsius", "\\centercolon", "\\centerdot", "\\centernot", "\\centerOver", "\\cfrac", "\\check", 
    "\\checkmark", "\\chi", "\\choose", "\\circ", "\\circeq", "\\circlearrowleft", "\\circlearrowright", "\\circledast", "\\circledcirc", "\\circleddash", "\\circledR", 
    "\\circledS", "\\clap", "\\class", "\\clubsuit", "\\colon", "\\colonapprox", "\\Colonapprox", "\\coloneq", "\\Coloneq", "\\coloneqq", "\\Coloneqq", "\\colonsim", 
    "\\Colonsim", "\\color", "\\colorbox", "\\columncolor", "\\comm", "\\commutator", "\\complement", "\\cong", "\\coprod", "\\cos", "\\cosecant", "\\cosh", "\\cosine", 
    "\\cot", "\\cotangent", "\\coth", "\\cp", "\\cr", "\\cramped", "\\crampedclap", "\\crampedllap", "\\crampedrlap", "\\crampedsubstack", "\\cross", "\\crossproduct", 
    "\\csc", "\\csch", "\\cssId", "\\cup", "\\Cup", "\\curl", "\\curlyeqprec", "\\curlyeqsucc", "\\curlyvee", "\\curlywedge", "\\curvearrowleft", "\\curvearrowright", 
    "\\dagger", "\\daleth", "\\dashedLine", "\\dashleftarrow", "\\dashrightarrow", "\\dashv", "\\dbinom", "\\dblcolon", "\\dd", "\\ddagger", "\\ddddot", "\\dddot", "\\ddot", 
    "\\ddots", "\\DeclareMathOperator", "\\DeclarePairedDelimiters", "\\DeclarePairedDelimitersX", "\\DeclarePairedDelimitersXPP", "\\def", "\\definecolor", "\\deg", "\\degree", "\\delta", "\\Delta", "\\derivative", "\\det", "\\determinant", "\\dfrac", "\\diagdown", "\\diagonalmatrix", "\\diagup", "\\diamond", "\\Diamond", "\\diamondsuit", "\\diffd", "\\differential", "\\digamma", "\\dim", "\\displaylines", "\\displaystyle", "\\div", "\\divergence", "\\divideontimes", "\\divsymbol", "\\dmat", "\\dot", "\\doteq", "\\Doteq", "\\doteqdot", "\\dotplus", "\\dotproduct", "\\dots", "\\dotsb", "\\dotsc", "\\dotsi", "\\dotsm", "\\dotso", "\\doublebarwedge", "\\doublecap", "\\doublecup", "\\downarrow", "\\Downarrow", "\\downdownarrows", "\\downharpoonleft", "\\downharpoonright", "\\dv", "\\dyad", "\\ell", "\\empheqbigl", "\\empheqbiglangle", "\\empheqbiglbrace", "\\empheqbiglbrack", "\\empheqbiglceil", "\\empheqbiglfloor", "\\empheqbiglparen", "\\empheqbiglvert", "\\empheqbiglVert", "\\empheqbigr", "\\empheqbigrangle", "\\empheqbigrbrace", "\\empheqbigrbrack", "\\empheqbigrceil", "\\empheqbigrfloor", "\\empheqbigrparen", "\\empheqbigrvert", "\\empheqbigrVert", "\\empheql", "\\empheqlangle", "\\empheqlbrace", "\\empheqlbrack", "\\empheqlceil", "\\empheqlfloor", "\\empheqlparen", "\\empheqlvert", "\\empheqlVert", 
    "\\empheqr", "\\empheqrangle", "\\empheqrbrace", "\\empheqrbrack", "\\empheqrceil", "\\empheqrfloor", "\\empheqrparen", "\\empheqrvert", "\\empheqrVert", "\\emptyset", 
    "\\enclose", /*"\\end",*/ "\\enspace", "\\epsilon", "\\eqalign", "\\eqalignno", "\\eqcirc", "\\eqcolon", "\\Eqcolon", "\\eqqcolon", "\\Eqqcolon", "\\eqref", "\\eqsim", 
    "\\eqslantgtr", "\\eqslantless", "\\equiv", "\\erf", "\\eta", "\\eth", "\\ev", "\\eval", "\\evaluated", "\\exists", "\\exp", "\\expectationvalue", "\\exponential", 
    "\\expval", "\\fallingdotseq", "\\fbox", "\\fCenter", "\\fcolorbox", "\\fderivative", "\\fdv", "\\Finv", "\\flat", "\\flatfrac", "\\forall", "\\frac", "\\frak", 
    "\\framebox", "\\frown", "\\functionalderivative", "\\Game", "\\gamma", "\\Gamma", "\\gcd", "\\ge", "\\genfrac", "\\geq", "\\geqq", "\\geqslant", "\\gets", "\\gg", 
    "\\ggg", "\\gggtr", "\\gimel", "\\gnapprox", "\\gneq", "\\gneqq", "\\gnsim", "\\grad", "\\gradient", "\\gradientnabla", "\\grave", "\\gt", "\\gtrapprox", "\\gtrdot", 
    "\\gtreqless", "\\gtreqqless", "\\gtrless", "\\gtrsim", "\\gvertneqq", "\\hat", "\\hbar", "\\hbox", "\\hdashline", "\\heartsuit", "\\hfil", "\\hfill", "\\hfilll", 
    "\\hline", "\\hom", "\\hookleftarrow", "\\hookrightarrow", "\\hphantom", "\\href", "\\hskip", "\\hslash", "\\hspace", "\\huge", "\\Huge", "\\hypcosecant", "\\hypcosine", 
    "\\hypcotangent", "\\hypsecant", "\\hypsine", "\\hyptangent", "\\identitymatrix", "\\idotsint", "\\iff", "\\iiiint", "\\iiint", "\\iint", "\\Im", "\\imaginary", "\\imat", 
    "\\imath", "\\impliedby", "\\implies", "\\in", "\\inf", "\\infty", "\\injlim", "\\innerproduct", "\\int", "\\intercal", "\\intop", "\\iota", "\\ip", "\\it", "\\jmath", 
    "\\Join", "\\kappa", "\\ker", "\\kern", "\\ket", "\\Ket", "\\ketbra", "\\Ketbra", "\\label", "\\lambda", "\\Lambda", "\\land", "\\langle", "\\laplacian", "\\large", 
    "\\Large", "\\LARGE", "\\LaTeX", "\\lbrace", "\\lbrack", "\\lceil", "\\ldotp", "\\ldots", "\\le", "\\leadsto", "\\left", "\\Leftarrow", "\\leftarrow", "\\leftarrowtail", 
    "\\leftharpoondown", "\\leftharpoonup", "\\LeftLabel", "\\leftleftarrows", "\\Leftrightarrow", "\\leftrightarrow", "\\leftrightarrows", "\\leftrightharpoons", 
    "\\leftrightsquigarrow", "\\leftroot", "\\leftthreetimes", "\\leq", "\\leqalignno", "\\leqq", "\\leqslant", "\\lessapprox", "\\lessdot", "\\lesseqgtr", "\\lesseqqgtr", 
    "\\lessgtr", "\\lesssim", "\\let", "\\lfloor", "\\lg", "\\lgroup", "\\lhd", "\\lim", "\\liminf", "\\limits", "\\limsup", "\\ll", "\\LL", "\\llap", "\\llcorner", 
    "\\Lleftarrow", "\\lll", "\\llless", "\\lmoustache", "\\ln", "\\lnapprox", "\\lneq", "\\lneqq", "\\lnot", "\\lnsim", "\\log", "\\logarithm", "\\longleftarrow", 
    "\\Longleftarrow", "\\Longleftrightarrow", "\\longleftrightarrow", "\\longleftrightarrows", "\\longLeftrightharpoons", "\\longmapsto", "\\longrightarrow", 
    "\\Longrightarrow", "\\longrightleftharpoons", "\\longRightleftharpoons", "\\looparrowleft", "\\looparrowright", "\\lor", "\\lower", "\\lozenge", "\\lparen", 
    "\\lrcorner", "\\Lsh", "\\lt", "\\ltimes", "\\lvert", "\\lVert", "\\lvertneqq", "\\maltese", "\\mapsto", "\\mathbb", "\\mathbf", "\\mathbfcal", "\\mathbffrak", 
    "\\mathbfit", "\\mathbfscr", "\\mathbfsf", "\\mathbfsfit", "\\mathbfsfup", "\\mathbfup", "\\mathbin", "\\mathcal", "\\mathchoice", "\\mathclap", "\\mathclose", 
    "\\mathfrak", "\\mathinner", "\\mathit", "\\mathllap", "\\mathmakebox", "\\mathmbox", "\\mathnormal", "\\mathop", "\\mathopen", "\\mathord", "\\mathpunct", "\\mathrel", 
    "\\mathring", "\\mathrlap", "\\mathrm", "\\mathscr", "\\mathsf", "\\mathsfit", "\\mathsfup", "\\mathstrut", "\\mathtip", "\\mathtoolsset", "\\mathtt", "\\mathup", 
    "\\matrix", "\\matrixdeterminant", "\\matrixel", "\\matrixelement", "\\matrixquantity", "\\max", "\\mbox", "\\mdet", "\\measuredangle", "\\mel", "\\mho", "\\micro", 
    "\\mid", "\\middle", "\\min", "\\minCDarrowheight", "\\minCDarrowwidth", "\\mit", "\\mkern", "\\mmlToken", "\\mod", "\\models", "\\MoveEqLeft", "\\moveleft", 
    "\\moveright", "\\mp", "\\mqty", "\\mskip", "\\mspace", "\\MTFlushSpaceAbove", "\\MTFlushSpaceBelow", "\\MTThinColon", "\\mu", "\\multimap", "\\nabla", "\\natural", 
    "\\naturallogarithm", "\\ncong", "\\ndownarrow", "\\ne", "\\nearrow", "\\neg", "\\negmedspace", "\\negthickspace", "\\negthinspace", "\\neq", "\\newcommand", 
    "\\newenvironment", "\\Newextarrow", "\\newline", "\\newtagform", "\\nexists", "\\ngeq", "\\ngeqq", "\\ngeqslant", "\\ngtr", "\\ni", "\\nleftarrow", "\\nLeftarrow", 
    "\\nleftrightarrow", "\\nLeftrightarrow", "\\nleq", "\\nleqq", "\\nleqslant", "\\nless", "\\nmid", "\\nobreakspace", "\\nolimits", "\\noLine", "\\nonscript", 
    "\\nonumber", "\\norm", "\\normalsize", "\\not", "\\notag", "\\notChar", "\\notin", "\\nparallel", "\\nprec", "\\npreceq", "\\nrightarrow", "\\nRightarrow", 
    "\\nshortmid", "\\nshortparallel", "\\nsim", "\\nsubseteq", "\\nsubseteqq", "\\nsucc", "\\nsucceq", "\\nsupseteq", "\\nsupseteqq", "\\ntriangleleft", "\\ntrianglelefteq", 
    "\\ntriangleright", "\\ntrianglerighteq", "\\nu", "\\nuparrow", "\\nvdash", "\\nvDash", "\\nVdash", "\\nVDash", "\\nwarrow", "\\odot", "\\ohm", "\\oint", "\\oldstyle", 
    "\\omega", "\\Omega", "\\omicron", "\\ominus", "\\op", "\\operatorname", "\\oplus", "\\order", "\\ordinarycolon", "\\oslash", "\\otimes", "\\outerproduct", "\\over", 
    "\\overbrace", "\\overbracket", "\\overleftarrow", "\\overleftrightarrow", "\\overline", "\\overparen", "\\overrightarrow", "\\overset", "\\overunderset", 
    "\\overwithdelims", "\\owns", "\\parallel", "\\partial", "\\partialderivative", "\\paulimatrix", "\\pb", "\\pderivative", "\\pdv", "\\perp", "\\perthousand", "\\phantom", 
    "\\phi", "\\Phi", "\\pi", "\\Pi", "\\pitchfork", "\\pm", "\\pmat", "\\pmatrix", "\\pmb", "\\pmod", "\\pmqty", "\\Pmqty", "\\pod", "\\poissonbracket", "\\pqty", "\\Pr", 
    "\\prec", "\\precapprox", "\\preccurlyeq", "\\preceq", "\\precnapprox", "\\precneqq", "\\precnsim", "\\precsim", "\\prescript", "\\prime", "\\principalvalue", 
    "\\Probability", "\\prod", "\\projlim", "\\propto", "\\psi", "\\Psi", "\\pu", "\\pv", "\\PV", "\\qall", "\\qand", "\\qas", "\\qassume", "\\qc", "\\qcc", "\\qcomma", 
    "\\qelse", "\\qeven", "\\qfor", "\\qgiven", "\\qif", "\\qin", "\\qinteger", "\\qlet", "\\qodd", "\\qor", "\\qotherwise", "\\qq", "\\qqtext", "\\qquad", "\\qsince", 
    "\\qthen", "\\qty", "\\quad", "\\quantity", "\\QuaternaryInf", "\\QuaternaryInfC", "\\QuinaryInf", "\\QuinaryInfC", "\\qunless", "\\qusing", "\\raise", "\\rangle", 
    "\\rank", "\\rbrace", "\\rbrack", "\\rceil", "\\Re", "\\real", /* "\\ref", */ "\\refeq", "\\renewcommand", "\\renewenvironment", "\\renewtagform", "\\Res", "\\Residue", 
    "\\restriction", "\\rfloor", "\\rgroup", "\\rhd", "\\rho", "\\right", "\\Rightarrow", "\\rightarrow", "\\rightarrowtail", "\\rightharpoondown", "\\rightharpoonup", 
    "\\RightLabel", "\\rightleftarrows", "\\rightleftharpoons", "\\rightrightarrows", "\\rightsquigarrow", "\\rightthreetimes", "\\risingdotseq", "\\RL", "\\rlap", "\\rm", 
    "\\rmoustache", "\\root", "\\rootAtBottom", "\\rootAtTop", "\\rowcolor", "\\rparen", "\\Rrightarrow", "\\Rsh", "\\rtimes", "\\rule", "\\Rule", "\\rvert", "\\rVert", 
    "\\S", "\\sbmqty", "\\scr", "\\scriptscriptstyle", "\\scriptsize", "\\scriptstyle", "\\searrow", "\\sec", "\\secant", "\\sech", "\\set", "\\Set", "\\setminus", "\\sf", 
    "\\sharp", "\\shortmid", "\\shortparallel", "\\shortvdotswithin", "\\shoveleft", "\\shoveright", "\\sideset", "\\sigma", "\\Sigma", "\\sim", "\\simeq", "\\sin", "\\sine", 
    "\\singleLine", "\\sinh", "\\skew", "\\SkipLimits", "\\small", "\\smallfrown", "\\smallint", "\\smallmatrixquantity", "\\smallsetminus", "\\smallsmile", "\\smash", 
    "\\smdet", "\\smile", "\\smqty", "\\solidLine", "\\Space", "\\space", "\\spadesuit", "\\sphericalangle", "\\splitdfrac", "\\splitfrac", "\\spmqty", "\\sPmqty", 
    "\\sqcap", "\\sqcup", "\\sqrt", "\\sqsubset", "\\sqsubseteq", "\\sqsupset", "\\sqsupseteq", "\\square", "\\stackbin", "\\stackrel", "\\star", "\\strut", "\\style", 
    "\\subset", "\\Subset", "\\subseteq", "\\subseteqq", "\\subsetneq", "\\subsetneqq", "\\substack", "\\succ", "\\succapprox", "\\succcurlyeq", "\\succeq", "\\succnapprox", 
    "\\succneqq", "\\succnsim", "\\succsim", "\\sum", "\\sup", "\\supset", "\\Supset", "\\supseteq", "\\supseteqq", "\\supsetneq", "\\supsetneqq", "\\surd", "\\svmqty", 
    "\\swarrow", "\\symbb", "\\symbf", "\\symbfcal", "\\symbffrak", "\\symbfit", "\\symbfscr", "\\symbfsf", "\\symbfsfit", "\\symbfsfup", "\\symbfup", "\\symcal", 
    "\\symfrak", "\\symit", "\\symnormal", "\\symrm", "\\symscr", "\\symsf", "\\symsfit", "\\symsfup", "\\symtt", "\\symup", "\\tag", "\\tan", "\\tangent", "\\tanh", 
    "\\tau", "\\tbinom", "\\TeX", "\\text", "\\textacutedbl", "\\textasciiacute", "\\textasciibreve", "\\textasciicaron", "\\textasciicircum", "\\textasciidieresis", 
    "\\textasciimacron", "\\textasciitilde", "\\textasteriskcentered", "\\textbackslash", "\\textbaht", "\\textbar", "\\textbardbl", "\\textbf", "\\textbigcircle", 
    "\\textblank", "\\textborn", "\\textbraceleft", "\\textbraceright", "\\textbrokenbar", "\\textbullet", "\\textcelsius", "\\textcent", "\\textcentoldstyle", 
    "\\textcircledP", "\\textclap", "\\textcolonmonetary", "\\textcolor", "\\textcompwordmark", "\\textcopyleft", "\\textcopyright", "\\textcurrency", "\\textdagger", 
    "\\textdaggerdbl", "\\textdegree", "\\textdied", "\\textdiscount", "\\textdiv", "\\textdivorced", "\\textdollar", "\\textdollaroldstyle", "\\textdong", "\\textdownarrow", 
    "\\texteightoldstyle", "\\textellipsis", "\\textemdash", "\\textendash", "\\textestimated", "\\texteuro", "\\textexclamdown", "\\textfiveoldstyle", "\\textflorin", 
    "\\textfouroldstyle", "\\textfractionsolidus", "\\textgravedbl", "\\textgreater", "\\textguarani", "\\textinterrobang", "\\textinterrobangdown", "\\textit", 
    "\\textlangle", "\\textlbrackdbl", "\\textleftarrow", "\\textless", "\\textlira", "\\textllap", "\\textlnot", "\\textlquill", "\\textmarried", "\\textmho", 
    "\\textminus", "\\textmu", "\\textmusicalnote", "\\textnaira", "\\textnineoldstyle", "\\textnormal", "\\textnumero", "\\textohm", "\\textonehalf", "\\textoneoldstyle", 
    "\\textonequarter", "\\textonesuperior", "\\textopenbullet", "\\textordfeminine", "\\textordmasculine", "\\textparagraph", "\\textperiodcentered", "\\textpertenthousand", 
    "\\textperthousand", "\\textpeso", "\\textpm", "\\textquestiondown", "\\textquotedblleft", "\\textquotedblright", "\\textquoteleft", "\\textquoteright", "\\textrangle", 
    "\\textrbrackdbl", "\\textrecipe", "\\textreferencemark", "\\textregistered", "\\textrightarrow", "\\textrlap", "\\textrm", "\\textrquill", "\\textsection", 
    "\\textservicemark", "\\textsevenoldstyle", "\\textsf", "\\textsixoldstyle", "\\textsterling", "\\textstyle", "\\textsurd", "\\textthreeoldstyle", "\\textthreequarters", 
    "\\textthreesuperior", "\\texttildelow", "\\texttimes", "\\texttip", "\\texttrademark", "\\texttt", "\\texttwooldstyle", "\\texttwosuperior", "\\textunderscore", 
    "\\textup", "\\textuparrow", "\\textvisiblespace", "\\textwon", "\\textyen", "\\textzerooldstyle", "\\tfrac", "\\therefore", "\\theta", "\\Theta", "\\thickapprox", 
    "\\thicksim", "\\thinspace", "\\TIC", "\\tilde", "\\times", "\\tiny", "\\Tiny", "\\to", "\\toggle", "\\top", "\\tr", "\\Tr", "\\trace", "\\Trace", "\\triangle", 
    "\\triangledown", "\\triangleleft", "\\trianglelefteq", "\\triangleq", "\\triangleright", "\\trianglerighteq", "\\TrinaryInf", "\\TrinaryInfC", "\\tripledash", 
    "\\tt", "\\twoheadleftarrow", "\\twoheadrightarrow", "\\UIC", "\\ulcorner", "\\UnaryInf", "\\UnaryInfC", "\\underbrace", "\\underbracket", "\\underleftarrow", 
    "\\underleftrightarrow", "\\underline", "\\underparen", "\\underrightarrow", "\\underset", "\\unicode", "\\unlhd", "\\unrhd", "\\upalpha", "\\uparrow", "\\Uparrow", 
    "\\upbeta", "\\upchi", "\\updelta", "\\Updelta", "\\updownarrow", "\\Updownarrow", "\\upepsilon", "\\upeta", "\\upgamma", "\\Upgamma", "\\upharpoonleft", 
    "\\upharpoonright", "\\upiota", "\\upkappa", "\\uplambda", "\\Uplambda", "\\uplus", "\\upmu", "\\upnu", "\\upomega", "\\Upomega", "\\upomicron", "\\upphi", "\\Upphi", 
    "\\uppi", "\\Uppi", "\\uppsi", "\\Uppsi", "\\uprho", "\\uproot", "\\upsigma", "\\Upsigma", "\\upsilon", "\\Upsilon", "\\uptau", "\\uptheta", "\\Uptheta", "\\upuparrows", 
    "\\upupsilon", "\\Upupsilon", "\\upvarepsilon", "\\upvarphi", "\\upvarpi", "\\upvarrho", "\\upvarsigma", "\\upvartheta", "\\upxi", "\\Upxi", "\\upzeta", "\\urcorner", 
    "\\usetagform", "\\va", "\\var", "\\varDelta", "\\varepsilon", "\\varGamma", "\\variation", "\\varinjlim", "\\varkappa", "\\varLambda", "\\varliminf", "\\varlimsup", 
    "\\varnothing", "\\varOmega", "\\varphi", "\\varPhi", "\\varpi", "\\varPi", "\\varprojlim", "\\varpropto", "\\varPsi", "\\varrho", "\\varsigma", "\\varSigma", 
    "\\varsubsetneq", "\\varsubsetneqq", "\\varsupsetneq", "\\varsupsetneqq", "\\vartheta", "\\varTheta", "\\vartriangle", "\\vartriangleleft", "\\vartriangleright", 
    "\\varUpsilon", "\\varXi", "\\vb", "\\vcenter", "\\vdash", "\\vDash", "\\Vdash", "\\vdot", "\\vdots", "\\vdotswithin", "\\vec", "\\vectorarrow", "\\vectorbold", 
    "\\vectorunit", "\\vee", "\\veebar", "\\verb", "\\Vert", "\\vert", "\\vmqty", "\\vnabla", "\\vphantom", "\\vqty", "\\vu", "\\Vvdash", "\\wedge", "\\widehat", 
    "\\widetilde", "\\wp", "\\wr", "\\xcancel", "\\xhookleftarrow", "\\xhookrightarrow", "\\xi", "\\Xi", "\\xleftarrow", "\\xLeftarrow", "\\xleftharpoondown", 
    "\\xleftharpoonup", "\\xleftrightarrow", "\\xLeftrightarrow", "\\xleftrightharpoons", "\\xLeftrightharpoons", "\\xlongequal", "\\xmapsto", "\\xmat", "\\xmathstrut", 
    "\\xmatrix", "\\xrightarrow", "\\xRightarrow", "\\xrightharpoondown", "\\xrightharpoonup", "\\xrightleftharpoons", "\\xRightleftharpoons", "\\xtofrom", 
    "\\xtwoheadleftarrow", "\\xtwoheadrightarrow", "\\yen", "\\zeromatrix", "\\zeta", "\\zmat",
    ];
}

function getMathJaxEnvs() {
    return [
    "align", "align*", "alignat", "alignat*", "aligned", "alignedat", "array", "bmatrix", "Bmatrix", "bmatrix*", "Bmatrix*", "bsmallmatrix", "Bsmallmatrix", "bsmallmatrix*", 
    "Bsmallmatrix*", "cases", "cases*", "CD", "crampedsubarray", "dcases", "dcases*", "drcases", "drcases*", "empheq", "eqnarray", "eqnarray*", "equation", "equation*", 
    "flalign", "flalign*", "gather", "gather*", "gathered", "lgathered", "matrix", "matrix*", "multline", "multline*", "multlined", "numcases", "pmatrix", "pmatrix*", 
    "prooftree", "psmallmatrix", "psmallmatrix*", "rcases", "rcases*", "rgathered", "smallmatrix", "smallmatrix*", "split", "spreadlines", "subarray", "subnumcases", 
    "vmatrix", "Vmatrix", "vmatrix*", "Vmatrix*", "vsmallmatrix", "Vsmallmatrix", "vsmallmatrix*", "Vsmallmatrix*", "xalignat", "xalignat*", "xxalignat",
    ];
}


function getMathJaxTextCommands() {
    return [
    "\\begin", "\\end", "\\cite", "\\eqref", "\\ref",  
    ];
}