from werkzeug.exceptions import BadRequest

recipes = [
    {"id": 1, 
    "name": "Chocolate Coconut Balls", 
    "url": "http://www.forksnknives.com/2015/11/chocolate-coconut-balls-recipe.html", 
    "ingredients": ["4.5 cups coconut flakes", "200ml condensed milk", "5 oz melted semi sweet chocolate"], "method": "Lightly pulse coconut flakes. Add the condensed milk and vanilla extract. Mix well. Refrigerate for 10 minutes. Make balls out of it and freeze for 10 minutes. Melt the chocolate. With the help of a fork, dip each balls into the chocolate, let the excess drip and place again on the parchment paper. Refrigerate for 10-15 minutes. Coconut Chocolate Balls are ready."},

    {"id": 2, 
    "name": "Easy Rolo Pretzel Turtles", 
    "url": "https://www.garnishwithlemon.com/easy-rolo-pretzel-turtles/", 
    "ingredients": ["60 Circle-shaped pretzels or any other small-shaped pretzels", "60 Rolo candies unwrapped", "60 Pecan halves"], 
    "method": "Preheat oven to 350 degrees. Line a baking sheet with parchment paper. Arrange desired number of pretzels on baking sheet. Place one Rolo candy in the center of each pretzel. Bake for 4-5 minutes. Remove from oven and immediately top each warm Rolo with a pecan half. Allow to cool thoroughly. Store in a sealed container."},

    {"id": 3, 
    "name": "Easy Fudge", 
    "url": "https://dearcrissy.com/easy-3-ingredient-fudge-recipe/", 
    "ingredients": ["3 cups semisweet chocolate chips", "1 (14 ounce) can sweetened condensed milk", "1/4 cup butter", "Optional mix-ins: walnuts, candy, pretzels, etc."], 
    "method": "Add semi-sweet chocolate chips, sweetened condensed milk, and butter (or margarine, if that's all you have on hand) in large microwaveable bowl. Warm in microwave on medium until melted, about 3-5 minute. Be sure to stir about every minute. Pour fudge mixture into well-greased 8x8-inch glass baking dish. Refrigerate until set. Enjoy! :)"},

    {"id": 4, 
    "name": "Flourless Peanut Butter Cookies", 
    "url": "https://lifemadesweeter.com/flourless-3-ingredient-peanut-butter-cookes/", "ingredients": ["1 cup natural unsweetened peanut butter", "1 large egg", "1/2 cup granulated or golden monk fruit sweetener , plus more for sprinkling on the tops if desired"], 
    "method": "Preheat oven to 350 degrees F. Line a baking sheet with parchment paper or a silicone mat. In a large bowl, beat together the peanut butter and monk fruit sweetener until smooth. Add the egg and mix until well combined. Add optional ingredients, as desired. Use a medium (1.5 tablespoon) cookie scoop to make about 14 cookies. If you like the crystallized crunch, sprinkle tops of cookies with additional granulated monk fruit sweetener. Place dough balls on prepared baking sheet at least 2 inches apart, and then use a fork to flatten and form a criss-cross pattern. Bake in preheated oven for 9 to 11 minutes, until the cookies are just slightly browned on the bottom. Be careful not to over-bake as the cookies will continue to cook. Allow to cool on the baking sheet for at least 20 minutes before transferring to a wire rack."},

    {"id": 5, 
    "name": "Easiest Nutella Brownies", 
    "url": "https://kirbiecravings.com/easiest-3-ingredient-nutella-brownies/", 
    "ingredients": ["1  1/4 cup Nutella", "2 large eggs", "1/2 cup all purpose flour"], 
    "method": "Preheat oven to 350°F. Grease a 9 inch x 9 inch metal baking pan. Add all ingredients into a large bowl and mix until batter is smooth. Pour into baking pan and smooth top with spatula.Bake for about 15 minutes until toothpick inserted comes out clean. Be careful not to bake too long otherwise brownies will dry out. Let brownies cool and set before cutting and serving."},

    {"id": 6, 
    "name": "Coconut Macaroons", 
    "url": "https://livingsweetmoments.com/3-ingredient-coconut-macaroons/", 
    "ingredients": ["4 egg whites", "3 cups sweetened shredded coconut", "1/2 cup granulated sugar"], 
    "method": "Preheat oven to 350 degrees Fahrenheit. Line 2 sheet pans with parchment paper. In a bowl, whisk the egg whites until frothy. Add the sugar and mix. Add the coconut and mix with a spoon. Using a small ice cream scoop (or rounded spoon), place mounds of cookie dough onto the cookie sheet. Bake for 15-20 minutes or until browned on top. Let them cool before eating. Enjoy!"},

    {"id": 7, 
    "name": "Flourless Nutella Mug Cake", 
    "url": "https://kirbiecravings.com/3-ingredient-flourless-nutella-mug-cake/", 
    "ingredients": ["1/4 cup Nutella", "1 large egg", "1/2 tbsp dutch processed cocoa powder"], 
    "method": "Combine all ingredients in an oversized microwave-safe mug. Mix vigorously with a small whisk until batter is smooth and the egg has been completely mixed in. Cook in the microwave for about 1 minute 10 seconds. The cake should be set but may be slightly wet on top. Let cake cool for 15 minutes before serving. The cake will condense down during this cooling process. You can replate in a smaller mug/plate/ramekin before serving. You can top with powdered sugar or chocolate syrup."},

]

def index(req):
    return [r for r in recipes], 200


def show(req, uid):
    return find_by_uid(uid), 200


def create(req):
    new_recipe = req.get_json()
    new_recipe['id'] = sorted([r['id'] for r in recipes])[-1] + 1
    recipes.append(new_recipe)
    return new_recipe, 201


def find_by_uid(uid):
    try:
        return next(r for r in recipes if r['id'] == uid)
    except:
        raise BadRequest(f"We don't have a recipe with id {uid}!")