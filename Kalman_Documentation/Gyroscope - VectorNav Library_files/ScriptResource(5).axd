Type.registerNamespace("Telerik.Sitefinity.Services.Search.Web.UI.Public");

Telerik.Sitefinity.Services.Search.Web.UI.Public.SearchBox = function (element) {
    Telerik.Sitefinity.Services.Search.Web.UI.Public.SearchBox.initializeBase(this, [element]);

    this._searchTextBox = null;
    this._searchButton = null;
    this._wordsMode = null;
    this._resultsUrl = null;
    this._indexCatalogue = null;

    this._keyPressDelegate = null;
    this._clickDelegate = null;
}

Telerik.Sitefinity.Services.Search.Web.UI.Public.SearchBox.prototype = {

    initialize: function () {
        Telerik.Sitefinity.Services.Search.Web.UI.Public.SearchBox.callBaseMethod(this, "initialize");

        if (this._searchTextBox) {
            this._keyPressDelegate = Function.createDelegate(this, this._keyPressHandler);
            $addHandler(this._searchTextBox, "keypress", this._keyPressDelegate);
        }

        if (this._searchButton) {
            this._clickDelegate = Function.createDelegate(this, this._clickHandler);
            $addHandler(this._searchButton, "click", this._clickDelegate);
        }
    },

    dispose: function () {
        if (this._searchTextBox && this._keyPressDelegate) {
            if (this._searchTextBox) {
                $removeHandler(this._searchTextBox, "keypress", this._keyPressDelegate);
            }
            delete this._keyPressDelegate;
        }
        if (this._searchButton && this._clickDelegate) {
            if (this._searchButton) {
                $removeHandler(this._searchButton, "click", this._clickDelegate);
            }
            delete this._clickDelegate;
        }
        Telerik.Sitefinity.Services.Search.Web.UI.Public.SearchBox.callBaseMethod(this, "dispose");
    },

    /* -------------------- Public methods ---------------- */

    navigateToResults: function (e) {
        if (!e) var e = window.event;

        if (e.stopPropagation) {
            e.stopPropagation();
        }
        else {
            e.cancelBubble = true;
        }
        if (e.preventDefault) {
            e.preventDefault();
        }
        else {
            e.returnValue = false;
        }

        if (this._searchTextBox.value && this._indexCatalogue) {
            window.location = this.getLocation();
        }
    },

    getLocation: function () {
        var query = this._searchTextBox.value;
        var separator = (this._resultsUrl.indexOf("?") == -1) ? "?" : "&";
        var indexCatalogue = String.format("{0}indexCatalogue={1}", separator, Url.encode(this._indexCatalogue));
        var searchQuery = String.format("&searchQuery={0}", Url.encode(query));
        var wordsMode = String.format("&wordsMode={0}", this._wordsMode);
        var url = this._resultsUrl + indexCatalogue + searchQuery + wordsMode;

        return url;
    },

    /* -------------------- Event handlers ---------------- */

    _keyPressHandler: function (e) {
        if (!e) var e = window.event;

        var keyCode = null;
        if (e.keyCode) {
            keyCode = e.keyCode;
        }
        else {
            keyCode = e.charCode;
        }

        if (keyCode == 13) {
            this.navigateToResults(e);
        }
    },

    _clickHandler: function (e) {
        this.navigateToResults(e);
    },

    /* -------------------- properties ---------------- */

    get_searchTextBox: function () {
        return this._searchTextBox;
    },
    set_searchTextBox: function (value) {
        this._searchTextBox = value;
    },

    get_searchButton: function () {
        return this._searchButton;
    },
    set_searchButton: function (value) {
        this._searchButton = value;
    },

    get_wordsMode: function () {
        return this._wordsMode;
    },
    set_wordsMode: function (value) {
        this._wordsMode = value;
    },

    get_resultsUrl: function () {
        return this._resultsUrl;
    },
    set_resultsUrl: function (value) {
        this._resultsUrl = value;
    },

    get_indexCatalogue: function () {
        return this._indexCatalogue;
    },
    set_indexCatalogue: function (value) {
        this._indexCatalogue = value;
    }
};
Telerik.Sitefinity.Services.Search.Web.UI.Public.SearchBox.registerClass("Telerik.Sitefinity.Services.Search.Web.UI.Public.SearchBox", Sys.UI.Control);

Telerik.Sitefinity.Services.Search.Web.UI.Public.WordsMode = function () {
    /// <summary>
    /// Represents the different client side words modes
    /// </summary>
};

Telerik.Sitefinity.Services.Search.Web.UI.Public.WordsMode.prototype = {
    AllWords: 0,
    AnyWord: 1
};
Telerik.Sitefinity.Services.Search.Web.UI.Public.WordsMode.registerEnum("Telerik.Sitefinity.Services.Search.Web.UI.Public.WordsMode");
