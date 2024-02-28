# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from frappe import _

def get():
	return {
		_("تطبيق الأموال (الأصول)"): {
			_("الأصول الحالية"): {
				_("المدينون"): {"account_type": "Receivable", "account_number": "1310"},
				_("الحسابات البنكية"): {"account_type": "Bank", "is_group": 1, "account_number": "1200"},
				_("النقد في الخزينة"): {
					_("النقد"): {"account_type": "Cash", "account_number": "1110"},
					"account_type": "Cash",
					"account_number": "1100",
				},
				_("القروض والسلف (الأصول)"): {
					_("سلف الموظفين"): {"account_number": "1610"},
					"account_number": "1600",
				},
				_("الأوراق المالية والودائع"): {
					_("مبلغ عربون"): {"account_number": "1651"},
					"account_number": "1650",
				},
				_("أصول المخزون"): {
					_("البضائع في اليد"): {"account_type": "Stock", "account_number": "1410"},
					"account_type": "Stock",
					"account_number": "1400",
				},
				_("أصول الضرائب"): {"is_group": 1, "account_number": "1500"},
				"account_number": "1100-1600",
			},
			_("الأصول الثابتة"): {
				_("معدات رأس المال"): {"account_type": "Fixed Asset", "account_number": "1710"},
				_("المعدات الإلكترونية"): {"account_type": "Fixed Asset", "account_number": "1720"},
				_("الأثاث والتجهيزات"): {"account_type": "Fixed Asset", "account_number": "1730"},
				_("معدات المكتب"): {"account_type": "Fixed Asset", "account_number": "1740"},
				_("المصانع والآلات"): {"account_type": "Fixed Asset", "account_number": "1750"},
				_("المباني"): {"account_type": "Fixed Asset", "account_number": "1760"},
				_("البرمجيات"): {"account_type": "Fixed Asset", "account_number": "1770"},
				_("الاهلاك المتراكم"): {
					"account_type": "Accumulated Depreciation",
					"account_number": "1780",
				},
				_("حساب الأعمال الرأسمالية قيد الإنشاء"): {"account_type": "Capital Work in Progress", "account_number": "1790"},
				"account_number": "1700",
			},
			_("الاستثمارات"): {"is_group": 1, "account_number": "1800"},
			_("الحسابات المؤقتة"): {
				_("الافتتاحية المؤقتة"): {"account_type": "Temporary", "account_number": "1910"},
				"account_number": "1900",
			},
			"root_type": "Asset",
			"account_number": "1000",
		},
		_("المصاريف"): {
			_("المصاريف المباشرة"): {
				_("مصروفات البضائع"): {
					_("تكلفة البضائع المباعة"): {"account_type": "Cost of Goods Sold", "account_number": "5111"},
					_("المصروفات المدرجة في تقييم الأصول"): {
						"account_type": "Expenses Included In Asset Valuation",
						"account_number": "5112",
					},
					_("المصروفات المدرجة في التقييم"): {
						"account_type": "Expenses Included In Valuation",
						"account_number": "5118",
					},
					_("تعديلات المخزون"): {"account_type": "Stock Adjustment", "account_number": "5119"},
					"account_number": "5110",
				},
				"account_number": "5100",
			},
			_("المصاريف غير المباشرة"): {
				_("المصروفات الإدارية"): {"account_number": "5201"},
				_("عمولة على المبيعات"): {"account_number": "5202"},
				_("الاهلاك"): {"account_type": "Depreciation", "account_number": "5203"},
				_("مصروفات الترفيه"): {"account_number": "5204"},
				_("تكاليف الشحن والتوصيل"): {"account_type": "Chargeable", "account_number": "5205"},
				_("المصروفات القانونية"): {"account_number": "5206"},
				_("مصروفات التسويق"): {"account_type": "Chargeable", "account_number": "5207"},
				_("صيانة المكاتب"): {"account_number": "5208"},
				_("إيجار المكاتب"): {"account_number": "5209"},
				_("المصروفات البريدية"): {"account_number": "5210"},
				_("الطباعة والأدوات المكتبية"): {"account_number": "5211"},
				_("تقريب الأرقام"): {"account_type": "Round Off", "account_number": "5212"},
				_("الراتب"): {"account_number": "5213"},
				_("مصروفات المبيعات"): {"account_number": "5214"},
				_("مصروفات الهاتف"): {"account_number": "5215"},
				_("مصروفات السفر"): {"account_number": "5216"},
				_("مصروفات المرافق"): {"account_number": "5217"},
				_("تكبير/تصغير الخسائر"): {"account_number": "5218"},
				_("الربح/الخسارة عند بيع الأصول"): {"account_number": "5220"},
				_("المصروفات المتنوعة"): {"account_type": "Chargeable", "account_number": "5221"},
				"account_number": "5200",
			},
			"root_type": "Expense",
			"account_number": "5000",
		},
		_("الإيرادات"): {
			_("الإيرادات المباشرة"): {
				_("المبيعات"): {"account_number": "4110"},
				_("الخدمات"): {"account_number": "4120"},
				"account_number": "4100",
			},
			_("الإيرادات غير المباشرة"): {"is_group": 1, "account_number": "4200"},
			"root_type": "Income",
			"account_number": "4000",
		},
		_("مصدر الأموال (المطالبات)"): {
			_("المطالبات الحالية"): {
				_("الدائنون"): {"account_type": "Payable", "account_number": "2110"},
				_("مرتبات الموظفين المستحقة"): {"account_number": "2120"},
				"account_number": "2100",
			},
			"root_type": "Liability",
			"account_number": "2000",
		},
		_("حقوق الملكية"): {
			_("رأس المال"): {"account_type": "Equity", "account_number": "3100"},
			_("أرباح المساهمين المدفوعة"): {"account_type": "Equity", "account_number": "3200"},
			_("رصيد الافتتاح"): {"account_type": "Equity", "account_number": "3300"},
			_("الأرباح المحتجزة"): {"account_type": "Equity", "account_number": "3400"},
			"root_type": "Equity",
			"account_number": "3000",
		},
	}
