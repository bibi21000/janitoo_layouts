# -*- coding: utf-8 -*-
"""
    janitoo_layouts.models.utils
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains all related models.

"""
__license__ = """
    This file is part of Janitoo.

    Janitoo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Janitoo is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Janitoo. If not, see <http://www.gnu.org/licenses/>.

"""
__author__ = 'Sébastien GALLET aka bibi21000'
__email__ = 'bibi21000@gmail.com'
__copyright__ = "Copyright © 2014-2015 Sébastien GALLET aka bibi21000"
import logging
logger = logging.getLogger( "janitoo.layouts" )
import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref
from janitoo_db.helpers import CRUDMixin
from janitoo_db.base import Base

def extend( jntmodel ):

    class LayoutsCategories(Base, CRUDMixin):
        __tablename__ = "core_layouts_categories"

        key = sa.Column(sa.String(255), primary_key=True)
        name = sa.Column(sa.String(255), nullable=False)
        description = sa.Column(sa.Text, nullable=False)
        layouts = relationship("Layouts", lazy="dynamic", backref="category",
                                   cascade="all, delete-orphan")
    jntmodel.LayoutsCategories = LayoutsCategories

    class Layouts(Base, CRUDMixin):
        __tablename__ = "core_layouts"

        key = sa.Column(sa.String(255), primary_key=True)
        value = sa.Column(sa.PickleType, nullable=False)
        layoutcategory = sa.Column(sa.String,
                                  sa.ForeignKey('core_layouts_categories.key',
                                                use_alter=True,
                                                name="fk_layouts_categories"),
                                  nullable=False)

        # The name (displayed in the form)
        name = sa.Column(sa.String(200), nullable=False)

        # The description (displayed in the form)
        description = sa.Column(sa.Text, nullable=False)

        @classmethod
        def get_all(cls):
            return cls.query.all()

        @classmethod
        def get_layouts(cls, from_group=None):
            """This will return all layouts with the key as the key for the dict
            and the values are packed again in a dict which contains
            the remaining attributes.

            :param from_group: Optionally - Returns only the layouts from a group.
            """
            result = None
            if from_group is not None:
                result = from_group.layouts
            else:
                result = cls.query.all()
            layouts = {}
            for layout in result:
                layouts[layout.key] = {
                    'name': layout.name,
                    'description': layout.description,
                }
            return layouts

        @classmethod
        def as_dict(cls, from_group=None, upper=True):
            """Returns all layouts as a dict. This method is cached. If you want
            to invalidate the cache, simply execute ``self.invalidate_cache()``.

            :param from_group: Returns only the layouts from the group as a dict.
            :param upper: If upper is ``True``, the key will use upper-case
                          letters. Defaults to ``False``.
            """

            layouts = {}
            result = None
            if from_group is not None:
                result = LayoutsCategories.query.filter_by(key=from_group).\
                    first()
                if result:
                    result = result.layouts
                else:
                    result = []
            else:
                #~ print(Setting.query)
                result = cls.query.all()
            #~ print result
            for layout in result:
                if upper:
                    layout_key = layout.key.upper()
                else:
                    layout_key = layout.key

                layouts[layout_key] = layout.value
            return layouts

    jntmodel.Layouts = Layouts
